## 1. Why did merging update-message-b cause a conflict, but merging update-message-a did not?

Main is the main version of the code/project. update-message-b caused a conflict because it changed the same line that had already changed on main, so then Git can’t decide which change to keep. update-message-a did not cause a conflict because main had not changed.

## 2. In the conflict markers, what does the section under HEAD represent? What does the section under the branch name represent?

HEAD is just a pointer that points to the current branch, representing the current code. The section under the branch name represents the code that comes from the branch which is being merged.

## 3. What command would abort a merge in progress if you decided not to resolve it?

git merge --abort
This cancels a merge that is in progress.

## 4. How does the git log --graph shape from Part C differ from the one in Part B? Why?

In Part B, the graph is a single line because the branch was simply merged directly into main. In Part C, the graph splits and comes back together because two branches were merged rather than being directly merged into main.
