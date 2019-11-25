#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "nrutil.h"

main(argc,argv)
int argc;
char **argv;
{

   int ndata;
   char curr;
   int i, j;
   double pi;
   double *r,*rray,*theta,*phi,*phib,*n,*ndry,*nwet,*ninf;
   double *T, *P, *init_P; // creating arrays for temp, and pressure
   double *val_1, *val_2, *P_w; // creating arrays for the exponent values for the wet pressure contribution
   double input_phi0, phi0,r0;
   double input_dtheta, dtheta;
   double RH;
   double beta, Pb, Tb; // declaring the temperature gradient, sea-level pressure and temp respectively
   double grav, R, M_0; // declaring the acceleration due to gravity, the gas constant and molar mass of air 
   double logscale;
   int ntheta;
   FILE *fp,*gp;
   char infile[80],outfile[80];

   FILE *files[101]; // a file pointer, pointing to 101 RH data files for a given observed angle

   if (argc!=3)
      { fprintf(stderr,"\n Usage: refractray phi0(deg) dtheta(rad)\n\n");
      exit(1);
   }
	 
   /* sscanf(*++argv,"%s",infile);*/  /* input file name */
   // sscanf(*++argv,"%s",outfile);  /* output file name */
   sscanf(*++argv,"%lf",&input_phi0);    /* initial co-zenith angle */
   sscanf(*++argv,"%lf",&input_dtheta);    /* increment in theta */
   // sscanf(*++argv,"%lf",&RH); /* relative humidity in percent */

   for(int i = 0; i < 101; i++) {
      RH = i;
      phi0 = input_phi0;
      dtheta = input_dtheta;

      sprintf(outfile, "%.3fphi0_%03dRH.dat", phi0, i); /* output file name */
      files[i] = fopen(outfile, "w"); /* list of output files with output file name given above */


      pi=acos(-1.0);
      phi0=pi/2.0-phi0*pi/180.0;
      beta = -6.5; // temp gradient in K(km^-1)
      Pb = 1023; // sea-level pressure in hPa (1013.25)
      Tb = 301.65; // sea-level temp in K (288.15)
      grav = 9.80665;
      R = 8.31432;
      M_0 = 0.028964420; // in kg(mol)^-1
      r0=6365.5; 

      ntheta=(int)5.0*pi/180.0/dtheta;


      phi=dvector(0,ntheta-1);
      phib=dvector(0,ntheta-1);
      rray=dvector(0,ntheta-1);
      n=dvector(0,ntheta-1);
      theta=dvector(0,ntheta-1);
     
      T = dvector(0,ntheta-1); // initialising an array for temperatures
      P = dvector(0,ntheta-1); // intitalising an array for pressures
      init_P = dvector(0,ntheta-1);
      val_1 = dvector(0,ntheta-1); 
      val_2 = dvector(0,ntheta-1);
      P_w = dvector(0,ntheta-1);
     
      val_1[0] = 18.678 - ((Tb - 273.15) / 234.5);
      val_2[0] = (Tb - 273.15) / (Tb - 16.01);
      P_w[0] = (RH / 100) * 6.1121 * exp(val_1[0] * val_2[0]);

      theta[0]=0.0;
      rray[0]=r0;
      phi[0]=phi0;
      // printf("First phi value is: %f\n", phi[0]);
      T[0] = Tb;
      n[0]=1.0 + (77.6*Pb)/Tb/1e6 - (5.6*P_w[0])/Tb/1e6 + (3.75e5*P_w[0])/pow(Tb, 2)/1e6;
      phib[0]=pi/2.0-phi0;
   
      // printf("phi angle is phi[%f]\n", phi[i]);
      for (j=1;j<=ntheta;j++)
         {
            
            theta[j]=dtheta*j;
            // printf("theta angle is theta[%f]\n", theta[j]);
            rray[j]=rray[j-1]*sin(phi[j-1]-theta[j-1])/sin(phi[j-1]-theta[j]);

            T[j] = (beta * (rray[j] - rray[0])) + Tb;
            init_P[j] = (((beta * (rray[j] - rray[0])) + Tb)) / Tb; // (in hPa)
            double exp_P =  (-grav * M_0 * 1000) / (beta * R);
            P[j] = Pb * pow(init_P[j], exp_P);
            
            val_1[j] = 18.678 - ((T[j] - 273.15) / 234.5);
            val_2[j] = (T[j] - 273.15) / (T[j] - 16.01);
            P_w[j] = (RH / 100) * 6.1121 * exp(val_1[j] * val_2[j]);


            //  n[i]=1.0+330.0/exp((rray[i]-rray[0])/8.0)/1e6; /* REPLACE THIS WITH SOMETHING BETTER */
            n[j] = 1 + (77.6 * P[j]/T[j])/1e6 - (5.6 * P_w[j])/T[j]/1e6 + (3.75e5 * P_w[j])/pow(T[j], 2)/1e6;

            phi[j]=asin(n[0]*rray[0]*sin(phi[0])/n[j]/rray[j])+theta[j];
            phib[j]=atan((rray[j]*cos(theta[j])-rray[0])/(rray[j]*sin(theta[j]))); /* bhatdotrhatv */       
            }

      gp=fopen(outfile,"w");
      // fprintf(gp,"#theta R n z T P_w\n");
      for (j=0;j<ntheta;j++)
         {
            fprintf(gp,"%.16g %.16g %.16g %.16g %.16g %.16g\n",theta[j],rray[j],n[j],phi[j]-theta[j],T[j],P_w[j]);
         }

      free_dvector(theta,0,ntheta-1);
      free_dvector(rray,0,ntheta-1);
      free_dvector(phi,0,ntheta-1);
      free_dvector(phib,0,ntheta-1);
      free_dvector(n,0,ntheta-1);

      free_dvector(T,0,ntheta-1); // free the memory allocation of the T vector
      free_dvector(P,0,ntheta-1);
      free_dvector(init_P,0,ntheta-1);
      free_dvector(val_1,0,ntheta-1); 
      free_dvector(val_2,0,ntheta-1);
      free_dvector(P_w,0,ntheta-1);
   }
}