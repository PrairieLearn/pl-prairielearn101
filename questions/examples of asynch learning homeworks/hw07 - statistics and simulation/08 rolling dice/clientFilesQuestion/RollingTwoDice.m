% Generate row vectors for 10,000 rolls of each kind of die using randi
sixSided = randi(6,1,10000);
twentySided = randi(20,1,10000);

% Add the row vectors together
sumVector = sixSided + twentySided;

% Logically index to select sums > 15 and count these
sumsOver15 = sumVector > 15;
count = sum(sumsOver15);

% Divide by 10,000 to get percentage > 15
percentage = count/10000;

% Display probability sum > 15
disp(['The probability that the sum of the two dice']);
disp(['rolls will be greater than 15 is: ', num2str(percentage), '.']);







