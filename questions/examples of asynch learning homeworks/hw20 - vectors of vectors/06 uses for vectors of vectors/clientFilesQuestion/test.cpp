#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>

using namespace std;

// prints out a vector of vector of integers
void printVecOfVecsInts(const vector<vector<int>> &vecs2) {

  // traverse the outer vector
  for (size_t i = 0; i < vecs2.size(); ++i){ 

    cout << "{ ";

    // traverse the i-th inner vector
    for (size_t k = 0; k < vecs2.at(i).size(); ++k) {
      
      // print the element
      cout << vecs2.at(i).at(k) << " ";

    } // end loop on inner vector

    cout << "}" << endl;
    
  } // end loop on outer vector

} // end function

int main()
{
  // DO NOT CHANGE ANYTHING IN THE MAIN FUNCTION

  // declare data as a vector of vectors
  vector<vector<int>> data;

  // make a vector
  vector<int> v1 = {2, 8, 65, 12};
  vector<int> v2 = {-4, 0, 32, -5};
  vector<int> v3 = {1, -23, 9, 35};

  // add these vector to data
  data.push_back(v1);
  data.push_back(v2);
  data.push_back(v3);

  // print what is in data
  printVecOfVecsInts(data);

  cout << "The element in row 3 and column 2 is: " << data.at(2).at(1) << endl;

}