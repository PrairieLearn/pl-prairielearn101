#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

#include "../clientFilesQuestion/analyzeData.h"

using namespace std;

int main(int argc, char *argv[]) {
  


  /* Saves stdout in a new file descriptor */
  int realStdoutNo = dup(STDOUT_FILENO);
  FILE *realStdout = fdopen(realStdoutNo, "w");

  /* Switches stdout/stderr to point to different file descriptor to
   * avoid students passing code by printing the correct result. */
  int devNull = open("/dev/null", O_WRONLY);
  dup2(devNull, STDOUT_FILENO);
  dup2(devNull, STDERR_FILENO);

  string inputFilename;
  //scanf("%d", &inputFilename);

  // load the tasks file
	ifstream dataIn(inputFilename);

	// Error check: see if the file opened correctly
	if (!dataIn.is_open())
	{
			cout << "Error: testData.txt could not be opened." << endl;
			return 1; // returning a nonzero value from main indicates an error
	}

	// get number of rows in the data
	string dummy; // dummy variable to store strings we need to skip over while reading data
	dataIn >> dummy; // skip the "numRows" label
	int numRows;
	dataIn >> numRows;

	// get number of columns in the data
	dataIn >> dummy; // skip the "numCols" label
	int numCols;
	dataIn >> numCols;

	// This is the "make space, then fill" pattern applied to a vector of vectors:

	// make a "row vector" of empty elements with the correct number "columns"
	vector < int > vec(numCols);

	// make a "matrix" of empty elements with the correct number of "rows" and "columns"
	vector < vector < int > > data(numRows, vec);

	// call the loadData function to "fill in" the "matrix"
	loadData(data, dataIn);
  
  dataIn.close();

  //fprintf(realStdout, "[%s]\n", square(n));

  printVecOfVecs(data);
  
  return 0;
}