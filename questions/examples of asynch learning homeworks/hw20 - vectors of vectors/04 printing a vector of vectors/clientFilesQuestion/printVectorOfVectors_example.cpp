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

  // declare v2 as a vector of vectors
  vector<vector<int>> v2;

  // make a vector
  vector<int> v = {1, 2, 3, 4};

  // add this vector to v2
  v2.push_back(v);

  // change v
  v.pop_back();

  // add new version of v to v2
  v2.push_back(v);

  // add a few elements to v
  for (int i = 6; i < 10; ++i){
    v.push_back(i);
  }

  // add new version of v to v2
  v2.push_back(v);

  // clear v
  v.clear();

  // add new version of v to v2
  v2.push_back(v);

  // add an element to v
  v.push_back(0);

  // add new version of v to v2
  v2.push_back(v);

  // print what is in v2
  printVecOfVecsInts(v2);

}