FROM mcr.microsoft.com/devcontainers/universal:2

# download the example course
RUN wget https://github.com/ace-lab/pl-ucb-csxxx/archive/b9ddf6afc0ba654844ca8cf7019ae5e586e933cc.zip
RUN unzip b9ddf6afc0ba654844ca8cf7019ae5e586e933cc
RUN mv pl-ucb-csxxx-b9ddf6afc0ba654844ca8cf7019ae5e586e933cc/ /pl-ucb-csxxx/
RUN rm b9ddf6afc0ba654844ca8cf7019ae5e586e933cc.zip
RUN chown -R codespace /pl-ucb-csxxx

# replace the element in the example course with the current version of the repo
RUN rm -rf /pl-ucb-csxxx/elements/pl-faded-parsons/

# prep for autograder jobs scheduling
RUN mkdir /tmp/pl_jobqueue
# RUN ln -s /workspaces/pl-faded-parsons/ /pl-ucb-csxxx/elements/pl-faded-parsons
