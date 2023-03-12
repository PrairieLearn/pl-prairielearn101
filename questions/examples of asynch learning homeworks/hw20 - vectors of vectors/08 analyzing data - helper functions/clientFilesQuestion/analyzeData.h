#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

void loadData(std::vector<std::vector<int> > &vec2, std::istream &input);
void sumOfRows(const std::vector<std::vector<int> > &data, std::vector<int> &row_sums);
void sumOfCols(const std::vector<std::vector<int> > &data, std::vector<int> &col_sums);
int sum(const std::vector<std::vector<int> > &vec2);
void printVecOfVecs(const std::vector<std::vector<int> > &vecs);
void printVecOfInts(const std::vector<int> &vec);