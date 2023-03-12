numRolls = 100000;

% Generate row vectors for the rolls of each die using randi
rolls1 = randi(6,1,numRolls);
rolls2 = randi(6,1,numRolls);

% Add the row vectors together
sumVector = rolls1 + rolls2;

% Logically index to select sums > 7 and count these
sumsOver7 = sumVector > 7;
count = sum(sumsOver7);

% Divide by 1,000 to get percentage > 7
percentage = count/numRolls;

% Display probability sum > 7
disp(['The probability that the sum of the two dice']);
disp(['rolls will be greater than 7 is: ', num2str(percentage), '.']);







