#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

#include "analyzeData.h"

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
	// using the >> operator and store each data point in an element of the 
	// vector of vectors.
	// Hint: use nested "for" loops to access each empty element






}

// calculates the sum of each row
// TODO implement this function
void sumOfRows(             ,               )
{






}

// calculates the sum of each column
// TODO implement this function
void sumOfCols(           ,                )
{







}

// calculates the sum of a vector of vectors of ints
// TODO implement this function
int sum(             )
{









}

// prints a vector of vectors of ints
void printVecOfVecs(const vector<vector<int> > &vecs)
{
	for (int i = 0; i < vecs.size(); ++i)
	{
		cout << "{ ";
		for (int k = 0; k < vecs.at(i).size(); ++k)
		{
			cout << vecs.at(i).at(k) << " ";
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
		cout << vec.at(k) << " ";
	}
	cout << "}" << endl;
}
