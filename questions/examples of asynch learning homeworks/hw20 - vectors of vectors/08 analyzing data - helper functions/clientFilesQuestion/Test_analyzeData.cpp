#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

#include "analyzeData.h"

using namespace std;


//The main function is written for you, but look through it to see how the functions are called
int main()
{

	// load the tasks file
	ifstream dataIn("testData.txt");

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
	/*  How to interpret this data variable:
		data is the outer vector; think of it as the "rows" in the "matrix"
		data.at(i) is the inner vector; think of it as one single row of the matrix
		data.at(i).at(j) is one element of the matrix (row i, column j)
		So, the "row index" is the first index, and the "column index" is the second index. 
		To get to a column, you MUST first select a row, THEN you can access a column. 
	*/

	// call the loadData function to "fill in" the "matrix"
	loadData(data, dataIn);

	// check to see if the data was read in correctly 
	// (comment these lines out after you verify that the data is read in correctly)
	cout << "Here is the input data: " << endl;
	printVecOfVecs(data);
	cout << endl;

	// calculate the sum value of each row
	// make a vector of the correct number of zeros (because zero is the additive identity)
	vector < int > row_sums(numRows, 0); 
	sumOfRows(data, row_sums);

	// calculate the sum value of each column
	// make a vector of the correct number of zeros (because zero is the additive identity)
	vector<int> col_sums(numCols, 0);
	sumOfCols(data, col_sums);

	// calculate the sum of the whole dataset
	int sumVal = sum(data); 

	// print results
	cout << "row sums: " << endl;
	printVecOfInts(row_sums);
	cout << endl;

	cout << "column sums: " << endl;
	printVecOfInts(col_sums);
	cout << endl;

	cout << "The sum of all the elements is: " << sumVal << endl;
}