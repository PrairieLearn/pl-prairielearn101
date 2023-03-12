#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

using namespace std;

// read data from an input stream into a vector of vectors
void loadData(vector<vector<int> > &vec2, istream &input)
{
	// Note: vec2 represents a rectangular matrix of empty elements

	// The number of "rows" is the size of the outer vector, vec2
	int numRows = vec2.size();

	// The number of "columns" is the size of one of the inner vectors; 
	// all of the inner vectors have the same size (since vec2 is modeling
	// a rectangular matrix), so we can use any inner vector we want to
	// get the number of the columns. Let's use the first inner vector.  
	int numCols = vec2.at(0).size();

	// TODO: implement the rest of the function to read in the data 
	// using the > > operator and store each data point in an element of the 
	// vector of vectors.
	// Hint: use nested "for" loops to access each empty element
	for (size_t i = 0; i < numRows; ++i) {
		for (size_t j = 0; j < numCols; ++j) {
			input >> vec2.at(i).at(j);
		}
	}

}

// calculates the sum of each row
// TODO implement this function
void sumOfRows(const vector<vector<int> > &data, vector<int> &row_sums)
{

	for (size_t iRow = 0; iRow < data.size(); ++iRow) {
		for (size_t iCol = 0; iCol < data.at(0).size(); ++iCol) {
			row_sums.at(iRow) += data.at(iRow).at(iCol);
		}
	}


}

// calculates the sum of each column
// TODO implement this function
void sumOfCols(const vector<vector<int> > &data, vector<int> &col_sums)
{

	for (size_t iCol = 0; iCol < data.at(0).size(); ++iCol) {
		for (size_t iRow = 0; iRow < data.size(); ++iRow) {
			col_sums.at(iCol) += data.at(iRow).at(iCol);
		}
	}

}

// calculates the sum of a vector of vectors of ints
// TODO implement this function
int sum(const vector<vector<int> > &vec2)
{
	int total = 0; // additive identity

	for (size_t i = 0; i < vec2.size(); ++i) {
		for (size_t j = 0; j < vec2.at(0).size(); ++j) {
			total += vec2.at(i).at(j);
		}
	}

	return total;

}

// prints a vector of vectors of ints
void printVecOfVecs(const vector<vector<int> > &vecs)
{
	for (int i = 0; i < vecs.size(); ++i)
	{
		cout << "{ ";
		for (int k = 0; k < vecs[i].size(); ++k)
		{
			cout << vecs[i][k] << " ";
		}
		cout << "}" << endl;
	}
}

// print a vector of ints
void printVecOfInts(const vector<int> &vec)
{
	cout << "{ ";
	for (int k = 0; k < vec.size(); ++k)
	{
		cout << vec[k] << " ";
	}
	cout << "}" << endl;
}



//The main function is written for you, but look through it to see how the functions are called
int main()
{

	cout << "STARTING TEST... " << endl;

	// get what test case this is
	int testCase;
	scanf("%i", &testCase);

	cout << "test case: " << testCase << endl;

	// determine which data file to use
	string inputFilename;
	if (testCase <=4) {
		inputFilename = "../tests/testData.txt";
	}
	else {
		inputFilename = "../tests/testData2.txt";
	}

	cout << "file: " << inputFilename << endl;


	char buff[FILENAME_MAX]; //create string buffer to hold path
	getcwd( buff, FILENAME_MAX );
	string current_working_dir(buff);
	cout << "current directory:" << current_working_dir << endl;


	// open the file stream
	ifstream dataIn(inputFilename);

	// Error check: see if the file opened correctly
	if (!dataIn.is_open())
	{
			cout << "Error: file could not be opened." << endl;
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
	if (testCase == 1 || testCase == 5) {
		printVecOfVecs(data);
		cout << endl;
	}

	// test sumOfRows function
	if (testCase == 2 || testCase == 6) {
		vector < int > row_sums(numRows, 0); 
		sumOfRows(data, row_sums);
		printVecOfInts(row_sums);
		cout << endl;
	}

	// test sumOfCols function
	if (testCase == 3 || testCase == 7) {
		vector<int> col_sums(numCols, 0);
		sumOfCols(data, col_sums);
		printVecOfInts(col_sums);
		cout << endl;
	}

	// test sum function
	if (testCase == 4 || testCase == 8) {
		cout << sum(data) << endl;
	}

}
