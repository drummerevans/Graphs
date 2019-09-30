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
     double pi;
     double *r,*rray,*theta,*phi,*phib,*n,*ndry,*nwet,*ninf;
     double phi0,r0;
     double dtheta;
     double logscale;
     int ntheta;
     FILE *fp,*gp;
     char infile[80],outfile[80];


     if (argc!=4)
       { fprintf(stderr,"\n Usage: refractray outfile phi0(deg) dtheta(rad)\n\n");
         exit(1);
	 }
	 
	 /* sscanf(*++argv,"%s",infile);*/  /* input file name */
         sscanf(*++argv,"%s",outfile);  /* output file name */
         sscanf(*++argv,"%lf",&phi0);    /* initial co-zenith angle */
         sscanf(*++argv,"%lf",&dtheta);    /* increment in theta */
         pi=acos(-1.0);
         phi0=pi/2.0-phi0*pi/180.0;
         r0=6365.5; 

     ntheta=(int)4.0*pi/180.0/dtheta;

     phi=dvector(0,ntheta-1);
     phib=dvector(0,ntheta-1);
     rray=dvector(0,ntheta-1);
     n=dvector(0,ntheta-1);
     theta=dvector(0,ntheta-1);

     theta[0]=0.0;
     rray[0]=r0;
     phi[0]=phi0;
     n[0]=1.0+330.0/1e6; 
     phib[0]=pi/2.0-phi0;

     for (i=1;i<=ntheta;i++)
        {
           theta[i]=dtheta*i;
           rray[i]=rray[i-1]*sin(phi[i-1]-theta[i-1])/sin(phi[i-1]-theta[i]);

           n[i]=1.0+330.0/exp((rray[i]-rray[0])/8.0)/1e6; /* REPLACE THIS WITH SOMETHING BETTER */

           phi[i]=asin(n[0]*rray[0]*sin(phi[0])/n[i]/rray[i])+theta[i];
           phib[i]=atan((rray[i]*cos(theta[i])-rray[0])/(rray[i]*sin(theta[i]))); /* bhatdotrhatv */       
         }

     gp=fopen(outfile,"w");
     fprintf(gp,"#theta R n z\n");
     for (i=0;i<ntheta;i++)
        {
           fprintf(gp,"%.16g %.16g %.16g %.16g\n",theta[i],rray[i],n[i],phi[i]-theta[i]);
        }

free_dvector(theta,0,ntheta-1);
free_dvector(rray,0,ntheta-1);
free_dvector(phi,0,ntheta-1);
free_dvector(phib,0,ntheta-1);
free_dvector(n,0,ntheta-1);
}

