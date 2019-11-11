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
     int i;
     double m;
     double pi;
     double *r,*rray,*theta,*phi,*phib,*n,*ndry,*nwet,*ninf;
     double *T, *P, *init_P; // creating arrays for temp, and pressure
     double *val_1, *val_2, *P_w; // creating arrays for the exponent values for the wet pressure contribution
     double phi0,r0;
     double dtheta;
     double RH;
     double RH_0;
     double beta, Pb, Tb; // declaring the temperature gradient, sea-level pressure and temp respectively
     double grav, R, M_0; // declaring the acceleration due to gravity, the gas constant and molar mass of air 
     double logscale;
     int ntheta;
     FILE *gp;
     char outfile[80];


     if (argc!=4)
       { fprintf(stderr,"\n Usage: cloud_refractray outfile phi0(deg) dtheta(rad)\n\n");
         exit(1);
	 }
	 
	 /* sscanf(*++argv,"%s",infile);*/  /* input file name */
         sscanf(*++argv,"%s",outfile);  /* output file name */
         sscanf(*++argv,"%lf",&phi0);    /* initial co-zenith angle */
         sscanf(*++argv,"%lf",&dtheta);    /* increment in theta */
         sscanf(*++argv,"%lf",&RH); /* relative humidity in percent */
         pi=acos(-1.0);
         phi0=pi/2.0-phi0*pi/180.0;
         beta = -6.5; // temp gradient in K(Km^-1)
         Pb = 1013.25; // sea-level pressure in hPa
         Tb = 288.15; // sea-level temp in K
         grav = 9.80665;
         R = 8.31432;
         M_0 = 0.028964420; // in kg(mol)^-1
         r0=6365.5; 

     ntheta=(int)4.0*pi/180.0/dtheta;					

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
     P_w[0] = (RH) * 6.1121 * exp(val_1[0] * val_2[0]);

     theta[0]=0.0;
     rray[0]=r0;
     phi[0]=phi0;
     T[0] = Tb;
     n[0]=1.0 + (77.6*Pb)/Tb/1e6 - (5.6*P_w[0])/Tb/1e6 + (3.75e5*P_w[0])/pow(Tb, 2)/1e6;
     phib[0]=pi/2.0-phi0;
   

     for (i=1;i<=ntheta;i++)
        {
           theta[i]=dtheta*i;
           rray[i]=rray[i-1]*sin(phi[i-1]-theta[i-1])/sin(phi[i-1]-theta[i]);
           
           m = -0.03;		// gradient of linear equation
           RH_0 = 70;		// initial relative humidity
           
           if (rray[i]<6369 && rray[i]>6367)			// assuming cloud cover between these altitudes
           	{
           		RH=98;
           	}
           else 
           	{
           		RH = m * (rray[i] - r0) + RH_0;
           	}

           T[i] = (beta * (rray[i] - rray[0])) + Tb;
           init_P[i] = (((beta * (rray[i] - rray[0])) + Tb)) / Tb; // (in hPa)
           double exp_P =  (-grav * 0.028964420 * 1000) / (beta * R);
           P[i] = Pb * pow(init_P[i], exp_P);
           
           val_1[i] = 18.678 - ((T[i] - 273.15) / 234.5);
           val_2[i] = (T[i] - 273.15) / (T[i] - 16.01);
           P_w[i] = (RH) * 6.1121 * exp(val_1[i] * val_2[i]);
         

          //  n[i]=1.0+330.0/exp((rray[i]-rray[0])/8.0)/1e6; /* REPLACE THIS WITH SOMETHING BETTER */
           n[i] = 1 + (77.6 * P[i]/T[i])/1e6 - (5.6 * P_w[i])/T[i]/1e6 + (3.75e5 * P_w[i])/pow(T[i], 2)/1e6;

           phi[i]=asin(n[0]*rray[0]*sin(phi[0])/n[i]/rray[i])+theta[i];
           phib[i]=atan((rray[i]*cos(theta[i])-rray[0])/(rray[i]*sin(theta[i]))); /* bhatdotrhatv */    

           // printf("%.16g %.16g %.16g %.16g %.16g %.16g\n",theta[i],rray[i],n[i],phi[i]-theta[i],T[i],P_w[i]);     // sanity check  
         }

     gp=fopen(outfile,"w");
     // fprintf(gp,"#theta R n z T P_w\n");
     for (i=0;i<ntheta;i++)
        {
           fprintf(gp,"%.16g %.16g %.16g %.16g %.16g %.16g\n",theta[i],rray[i],n[i],phi[i]-theta[i],T[i],P_w[i]);
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

