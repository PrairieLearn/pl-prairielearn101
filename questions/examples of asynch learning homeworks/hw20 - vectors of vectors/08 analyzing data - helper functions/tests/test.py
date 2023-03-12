#! /usr/bin/python3

import sys, math, sympy
import cgrader

# importing the modules
import os
import shutil



class DemoGrader(cgrader.CPPGrader):

    def tests(self):
        
        # trying to debug why the files won't open

        self.change_mode("/grade/tests/testData.txt", "744")
        self.change_mode("/grade/tests/testData2.txt", "744")
        
        
        # compile unit tests driver program with student implementation file
        self.test_compile_file('analyzeData.cpp', 'unit_tests', add_c_file="/grade/tests/unit_tests.cpp", flags=["-I/grade/tests", "-I/grade/student","-std=c++17"])

        # self.test_compile_file('analyzeData.cpp', 'unit_tests', add_c_file="/grade/tests/unit_tests.cpp", flags=["-I/grade/tests", "-I/grade/student","-std=c++11"])


        # self.test_compile_file('sample.cpp', 'unit_tests',flags=["-I/grade/tests", "-I/grade/student","-I/clientFilesQuestion","-std=c++11"])



        # this is for testing with the solution
        #self.test_compile_file('analyzeData_solution.cpp', 'main', main_file='/grade/tests/main.cpp')

        # test cases to run:
        # With testData.txt
        #     1. call loadData, call printVecOfVecs
        #     2. call sumOfRows, call printVecOfInts
        #     3. call sumOfCols, call printVecOfInts
        #     4. call sum
        # With testData2.txt
        #     5. call loadData, call printVecOfVecs
        #     6. call sumOfRows, call printVecOfInts
        #     7. call sumOfCols, call printVecOfInts
        #     8. call sum

        # the unit tests file is set up as: 
        # 1. read in the number of the test case
        # 2. do the test that corresponds to that number

        # so, this python file needs to know the correct 
        # output for each test case (I think?)
        correctOutput = [
            'loadData using the original data file \n{ 1 2 3 4 5 6 7 }\n{ 8 9 10 11 12 13 14 }\n{ 15 16 17 18 19 20 21 }\n{ 22 23 24 25 26 27 28 }\n{ 29 30 31 32 33 34 35 }',
            'sumOfRows using the original data file \n{ 28 77 126 175 224 }',
            'sumOfCols using the original data file \n{ 75 80 85 90 95 100 105 }',
            'sum using the original data file \n630',
            'loadData using a different data file \n{ 1 2 3 4 100 6 7 3 }\n{ 8 9 100 11 12 13 14 3 }\n{ 15 160 17 18 19 20 21 3 }\n{ 220 23 24 25 26 27 28 3 }\n{ 29 30 31 32 33 340 35 3 }\n{ 220 23 240 25 26 27 28 3 }',
            'sumOfRows using a different data file \n{ 126 170 273 376 533 592 }',
            'sumOfCols using a different data file \n{ 493 247 415 115 216 433 133 18 }',
            'sum using a different data file \n2070'
        ]


        for iTestCase in range(8):
            output  = correctOutput[iTestCase]
            self.test_run('./unit_tests', input=f'\n{iTestCase+1}\n', exp_output = output)
            
            
            


g = DemoGrader()
g.start()
