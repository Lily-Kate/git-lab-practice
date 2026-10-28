1. Why is 'Squash and Merge' preferable over standard merge commits for small feature
branches in team projects?

'Squash and Merge' combines all branch commits into a single clean commit on main.
Cleans up temporary "wip" or "fix" commits and keeps the repository history easier to read.
Basically, adding the functions and then adding their docstrings were separate commits,
but squash and merge puts them on main as one commit.

2. Describe the difference between 'Add single comment' and 'Start a review' on GitHub.
Why is batching important?

'Add single comment' posts a comment immediately, while Start a review lets you
submit all comments simultaneously. Batching avoids spamming team members
with a million individual notification emails. Basically if I have feedback on three different
lines, I can send all three comments together instead of notifying others three separate times.

3. How do Branch Protection Rules prevent accidental production breakage?

Branch protection rules restrict things like direct pushes to main. They can require changes to go
through the pull request process and can require an approving review before merging. Basically,
if I accidentally try to push code that's undesirable for any reason straight to main, rules
ensure the push must go through review first.

4. When a remote conflict occurs in a PR, why is it better to merge origin/main
into your feature branch locally rather than forcing a push?

Merging origin/main into your feature branch brings in the latest changes so then you can resolve
any of the conflicts, test your code, and push updates to that the same PR. For example, main had
the SUPER CALCULATOR header in the assignment while my branch had CALCULATOR V2, so merging let
me choose which header to keep and test it instead of just forcing my branch over someone else's work.
