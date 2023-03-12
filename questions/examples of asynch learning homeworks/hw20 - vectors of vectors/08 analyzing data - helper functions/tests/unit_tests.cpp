#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <unistd.h>
#include <filesystem>
namespace fs = std::filesystem;

#include "analyzeData.h"

using namespace std;





//The main function is written for you, but look through it to see how the functions are called
int main() {


// 	char buff[FILENAME_MAX]; //create string buffer to hold path
// 	getcwd( buff, FILENAME_MAX );
// 	string current_working_dir(buff);
// 	cout << "directory: " << current_working_dir << endl;
	
// 	cout << "does the analyzeData.h file exist? "; 
// 	cout << std::filesystem::exists("analyzeData.h") << endl;
	
// 	// DEBUGGING LIVE VERSION
	
// 	// open the file stream
// 	ifstream fin("analyzeData.h");
// 	// pretty sure this MUST exist because the program compiles and runs
	

// 	// Error check: see if the file opened correctly
// 	if (!fin.is_open())
// 	{
// 			cout << "Error: analyzeData.h could not be opened." << endl;
// 			return 1; // returning a nonzero value from main indicates an error
// 	}
	
// 	// print the first part of the file to see if it will work
// 	string temp;
// 	for (int i = 0; i < 25; ++i) {
// 	    fin >> temp;
// 	    cout << temp;
// 	}
// 	fin.close();
	
	
// 	std::string path = ".";
// 	for (const auto & entry : fs::directory_iterator(path))
// 			std::cout << entry.path() << std::endl;

	cout << "From Your Code: " << endl;

	// get what test case this is
	int testCase;
	scanf("%i", &testCase);

// 	cout << "test case: " << testCase << endl;

	// determine which data file to use
	string inputFilename;
	if (testCase <=4) {
		inputFilename = "../tests/testData.txt";
	}
	else {
		inputFilename = "../tests/testData2.txt";
	}

    
// 	cout << "file: " << inputFilename << endl;


	// open the file stream
	ifstream dataIn(inputFilename);

	// Error check: see if the file opened correctly
	if (!dataIn.is_open())
	{
			cout << "Error: data file could not be opened." << endl;
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
	/*  How to interpret this data variable:
		data is the outer vector; think of it as the "rows" in the "matrix"
		data.at(i) is the inner vector; think of it as one single row of the matrix
		data.at(i).at(j) is one element of the matrix (row i, column j)
		So, the "row index" is the first index, and the "column index" is the second index. 
		To get to a column, you MUST first select a row, THEN you can access a column. 
	*/

	// call the loadData function to "fill in" the "matrix"
	loadData(data, dataIn);
	dataIn.close();


	// --------- BEGIN UNIT TESTING --------------------//

	// test loadData function
	if (testCase == 1) {
		cout << "         loadData using the original data file " << endl;
		printVecOfVecs(data);
		cout << endl;
	}
	if (testCase == 5) {
		cout << "         loadData using a different data file " << endl;
		printVecOfVecs(data);
		cout << endl;
	}

	// test sumOfRows function
	if (testCase == 2) {
		cout << "         sumOfRows using the original data file " << endl;
		vector < int > row_sums(numRows, 0); 
		sumOfRows(data, row_sums);
		printVecOfInts(row_sums);
		cout << endl;
	}
	if (testCase == 6) {
		cout << "         sumOfRows using a different data file " << endl;
		vector < int > row_sums(numRows, 0); 
		sumOfRows(data, row_sums);
		printVecOfInts(row_sums);
		cout << endl;
	}

	// test sumOfCols function
	if (testCase == 3) {
		cout << "         sumOfCols using the original data file " << endl;
		vector<int> col_sums(numCols, 0);
		sumOfCols(data, col_sums);
		printVecOfInts(col_sums);
		cout << endl;
	}
	if (testCase == 7) {
		cout << "         sumOfCols using a different data file " << endl;
		vector<int> col_sums(numCols, 0);
		sumOfCols(data, col_sums);
		printVecOfInts(col_sums);
		cout << endl;
	}

	// test sum function
	if (testCase == 4) {
		cout << "         sum using the original data file " << endl;
		cout << sum(data) << endl;
	}
	if (testCase == 8) {
		cout << "         sum using a different data file " << endl;
		cout << sum(data) << endl;
	}

}
