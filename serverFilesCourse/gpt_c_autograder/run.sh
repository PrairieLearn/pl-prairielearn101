#! /bin/bash

# Generate the code
bash -c 'python3 /grade/serverFilesCourse/gpt_c_autograder/make_code.py'

if [ -s results.json ]
then
  # Let's attempt to keep everything from dying completely
  echo '{"succeeded": false, "score": 0.0, "message": "Failed to generate code via the AI. Please try again."}' > /grade/results/results.json
  exit -1
fi

bash -c "python3 /grade/tests/test.py"
bash -c "python3 /grade/serverFilesCourse/gpt_c_autograder/generate_feedback.py"
