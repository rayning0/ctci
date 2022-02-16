# Answers/Notes to [Cracking the Coding Interview, 6th Ed.](http://www.crackingthecodinginterview.com)

To join our [Slack CTCI study group](https://linkedin-jr-engineers.slack.com), **give me your email, [install Zoom](https://zoom.us/download), and create a [Zoom account](https://zoom.us/signup). Join Slack after I invite you by email.** Then I'll add you to our private Slack channel.

**We don't have weekly meetings now. If I have time in the future, I may restart this study group.**

---------------
See all my **[LeetCode solutions](https://github.com/rayning0/ctci/tree/master/leetcode)**.
My **[Codility solutions](https://github.com/rayning0/codility)**.
My **[Project Euler solutions](https://github.com/rayning0/ProjectEuler-and-Algorithms/tree/master/euler)**.
My **[HackerRank solutions](https://github.com/rayning0/ctci/tree/master/hackerrank)**.

In January 2020, we began solving the 150 coding questions from this course: **[Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview)**, as I explain [here](https://www.linkedin.com/posts/raymond-gan-0ba8011_grokking-the-coding-interview-patterns-for-activity-6630206560280944641-HO8Q) and [here](https://linkedin-jr-engineers.slack.com/archives/CDDPLUHQC/p1576004249125300). Buy the course for $79 to see it all. It's optional to buy the course. **[See all my coding answers for it](https://github.com/rayning0/ctci/tree/master/gtci)**.

---------------
See [our YouTube channel](https://www.youtube.com/channel/UCXd8p77ZB0sQbtk6mDyeqkw/about) for video of our group meetings. I don't update this much. You should come to our meetings.

See my 2.5 hour YouTube video interview: **[How to be competitive for software jobs](https://youtu.be/WqFOTeiSeEY)**, which covers **[my 5 LinkedIn articles for bootcamp grads](https://www.linkedin.com/in/raymond-gan-0ba8011/detail/recent-activity/posts/)**.

This group codes through company code challenge problems and all 189 coding interview questions in Gayle McDowell's book "Cracking the Coding Interview" together. We’ll try to solve 1+ company code challenge per meeting. To post code challenges for our group to solve, put them in our **[private Zoom Slack channel](https://linkedin-jr-engineers.slack.com/archives/GN87TNSH0)**. Use any computer language you wish.

Gayle McDowell's [crowdsourced CTCI solutions](https://github.com/careercup/CtCI-6th-Edition), by programming language.

Most software engineers study this book to interview at FAANG companies: Facebook, Apple, Amazon, Netflix, Google, Microsoft, etc.

I made these Slack channels for us. Please join them all:

- [#system-design-interviews](https://linkedin-jr-engineers.slack.com/archives/CTTP68RPZ) System Design Interviews
- [#leetcode](https://linkedin-jr-engineers.slack.com/messages/CL9UDQ4LS) LeetCode Problems
- [#hackerrank](https://linkedin-jr-engineers.slack.com/archives/CR8EP9AMU) HackerRank Problems
- [#project-euler](https://linkedin-jr-engineers.slack.com/archives/CQJ63PMEJ) Project Euler Problems
- [#ctci-big-o](https://linkedin-jr-engineers.slack.com/messages/CKTPDEEN6/) Big O Time/Space Complexity. Chapter VI.
- [#ctci-ch01](https://linkedin-jr-engineers.slack.com/messages/CL7AFTC6A/) Arrays, Strings, and Hashes
- [#ctci-ch02](https://linkedin-jr-engineers.slack.com/messages/CL930575L/) Linked Lists
- [#ctci-ch03](https://linkedin-jr-engineers.slack.com/messages/CL930EVPY/) Stacks and Queues
- [#ctci-ch04](https://linkedin-jr-engineers.slack.com/messages/CL0HVSS49/) Trees and Graphs
- [#ctci-ch08](https://linkedin-jr-engineers.slack.com/messages/CMY2R0VBK/) Recursion and Dynamic Programming
- [#eloquentjavascript](https://linkedin-jr-engineers.slack.com/messages/CDD6ZFLTS/) on JavaScript and that book.
- [#java](https://linkedin-jr-engineers.slack.com/archives/CQSD35KM1) Java
- [#python](https://linkedin-jr-engineers.slack.com/archives/CR3DDHPHS) Python
- [#ruby](https://linkedin-jr-engineers.slack.com/archives/CQR3NBUJE) Ruby

- Use the [#pair-programming](https://linkedin-jr-engineers.slack.com/messages/CL6UDFVSR/) channel to ask for help or offer to work together with others.
- Please [#introduce-yourself](https://linkedin-jr-engineers.slack.com/messages/CDG6ZSWMU/) and talk about your [#job-search](https://linkedin-jr-engineers.slack.com/messages/CDE3RK8QY/). Don't use the [#general](https://linkedin-jr-engineers.slack.com/messages/CDDPLUHQC/) channel to introduce yourself.

CTCI's [official Facebook group](https://www.facebook.com/groups/ctciofficial/).

CTCI's [official Slack group](https://crackinginterview.slack.com).

[VS Code](https://code.visualstudio.com/docs/languages/java) is my code editor. I installed its [Java Extension Pack](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack).

I cloned [Gayle's GitHub solutions](https://github.com/careercup/CtCI-6th-Edition) and opened the /Java folder in VS Code. It instantly told me what to install and let me start running/debugging code with breakpoints, with NO configuration! Super easy.

---

If you forked this GitHub repo to your laptop, here's **how to easily keep your fork up to date with mine as I add new code:**

In directory of your `/ctci` folder in the terminal, type:

1. `git remote add upstream git@github.com:rayning0/ctci.git`

2. `git fetch upstream`
3. `git pull upstream master`
4. `git push -f`

Line 1 adds a [remote repo](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) called "upstream" to your fork, pointing to my GitHub repo.

Lines 2-4 update what "upstream" means, pulls the latest code from my /ctci repo, then [force pushes](https://evilmartians.com/chronicles/git-push---force-and-how-to-deal-with-it) it up to YOUR repo.

Since I don't want to type all these lines, I added them to my [`.bash_profile`](https://natelandau.com/my-mac-osx-bash_profile/):

```
function grau { # update fork (part 1)
  git remote add upstream $1
}

function gupdate { # update fork (part 2)
  git fetch upstream
  git pull upstream master
  git push -f
}
```

You only need to type `grau git@github.com:rayning0/ctci.git` once.

In the future, as I add new code to my /ctci repo, just `cd` to YOUR /ctci fork of mine and type `gupdate`. It will automatically pull my latest code.

If you don't have a `.bash_profile`, create this file in your home directory. After editing it, run the file by doing [`source ~/.bash_profile`](https://stackoverflow.com/questions/4608187/how-to-reload-bash-profile-from-the-command-line).

**By Raymond Gan**
