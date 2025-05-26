# Hands-On Activity in Pairs

Now that we have seen how to work with git, we are going to do a simple exercise in which you'll get to try out a lot of the shown features! For this we'll work in pairs. Someone will be **Person A**, and the other **Person B**. Decide on it and then follow the following steps:

## Person A:

1. Fork the frp-workshop repository. This creates your own personal copy of it. Then, in your fork, go to Settings >> Collaborators >> Add People, and invite Person B with their Github handle.

2. Once Person B has joined, set up your SSH keys and clone the repository. You can find the instructions for this on the README.md file.

3. Create the branch **sum** and implement the sum method that takes in two values a and b, and outputs the sum. Push your new branch. This requires adding, commiting, setting upstream, pushing.

4. Merge the branch **sum** into the **main** branch. If succesful, delete the sum branch.

5. Wait until Person B finishes their step 4. Checkout to the main branch and pull the changes. Then, create branch **mul** and implement the mul method that takes in two values a and b, and outputs the multiplication. Push your new branch.

6. Wait until Person B has completed their step 6. Checkout to branch main and pull the changes. Then, merge branch **mul** to it by resolving the merge conflict. If succesful, delete the mul branch.

## Person B:

1. Accept the invitation to join the repository of Person A.

2. Set up your SSH keys and clone the repository. You can find the instructions for this on the README.md file.

3. Create the branch **sub** and implement the sub method that takes in two values a and b, and outputs the subtraction. Push your new branch. This requires adding, commiting, setting upstream, pushing.

4. Wait until Person A has completed their step 4. Checkout to branch main and pull the changes. Then, merge branch **sub** to it by resolving the merge conflict. If succesful, delete the sub branch.

5. Create branch **div** and implement the div method that takes in two values a and b, and outputs the divition. Push your new branch.

6. Merge the branch **div** into the **main** branch. If succesful, delete the div branch.

7. Wait until Person A finished their step 6. Then pull the changes on the main branch.