#include <stdio.h>
#include <stdlib.h>
#include "fdtd-macro.h"
#include <complex.h>
#include <math.h>
/*code to record a sensor of the data*/
void sensorInit(Grid *g, double Kx, double Ky, double Kz, int j){
	char filename[100];
	FILE *out;
	sprintf(filename, "PBGData/MultiPass3/EmptyLat%d.txt",j);
        out = fopen(filename, "a");
	fprintf(out, "%g \t %g \t %g \n", Kx, Ky, Kz);
	fclose(out);

return;
}



void Transmission(Grid *g, int j,  double time){
        char filename[100];
        double Time1;
        FILE *out;
        sprintf(filename, "PBGData/MultiPass3/EmptyLat%d.txt", j);
        out = fopen(filename, "a");
        Time1 = time*5.4683e-13;

        /* print the time stamp and the Ex field right before the QWS*/
        fprintf(out, "%g \t %g \t %g \t %g \t %g \t %g \t %g \t %g \t %g \t %g \t %g\n", Time1, creal(Hz(80, 17, 1)), cimag(Hz(80, 17, 1)), creal(Hz(260, 65, 1)), cimag(Hz(260, 65, 1)), creal(Hz(681, 77, 1)), cimag(Hz(681, 77, 1)), creal(Hz(904, 44, 1)), cimag(Hz(904, 44, 1)), creal(Hz(2277, 83, 1)), cimag(Hz(2277, 83, 1)));
        fclose(out);

        
        
}



