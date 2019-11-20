# Answers/Notes to [Cracking the Coding Interview, 6th Ed.](http://www.crackingthecodinginterview.com)

To join our [Slack CTCI study group](https://linkedin-jr-engineers.slack.com), **give me your email and your Skype name**.
See [our YouTube channel](https://www.youtube.com/channel/UCXd8p77ZB0sQbtk6mDyeqkw/about), with video of our beginner group meetings.

See my 2.5 hour YouTube video interview: **[How to be competitive for software jobs](https://youtu.be/WqFOTeiSeEY)**, which covers **[my 5 LinkedIn articles for bootcamp grads](https://www.linkedin.com/in/raymond-gan-0ba8011/detail/recent-activity/posts/)**.

Gayle McDowell's [crowdsourced CTCI solutions](https://github.com/careercup/CtCI-6th-Edition), by programming language.

This group will code through company code challenge problems and all 189 coding interview questions in Gayle McDowell's book "Cracking the Coding Interview" together. Use any language you wish. We’ll try to solve 1 company code challenge per hour. To post code challenges for our group to solve, put them in our **[private Skype Slack channel](https://linkedin-jr-engineers.slack.com/archives/GN87TNSH0)**.

**We meet 12 pm-2 pm PST on Skype each Saturday:**

- Please [install Skype](https://www.skype.com/en/get-skype/), create your account, and add me. My Skype name is **rayning3**.
- Please add your Skype name [in your Slack profile](https://get.slack.help/hc/en-us/articles/204092246-Edit-your-profile), so we can find you. Skype lets [up to 50 people](https://blogs.skype.com/news/2019/04/04/call-up-to-50-people-at-once-with-skype) in 1 call.

Most software engineers study this book to interview at FAANG companies: Facebook, Apple, Amazon, Netflix, Google, Microsoft, etc.

I made 13 Slack channels for us. Please join them:

- [#leetcode](https://linkedin-jr-engineers.slack.com/messages/CL9UDQ4LS) LeetCode Problems
- [#project-euler](https://linkedin-jr-engineers.slack.com/archives/CQJ63PMEJ) Project Euler Problems
- [#ctci-big-o](https://linkedin-jr-engineers.slack.com/messages/CKTPDEEN6/) Big O Time/Space Complexity. Chapter VI.
- [#ctci-ch01](https://linkedin-jr-engineers.slack.com/messages/CL7AFTC6A/) Arrays, Strings, and Hashes
- [#ctci-ch02](https://linkedin-jr-engineers.slack.com/messages/CL930575L/) Linked Lists
- [#ctci-ch03](https://linkedin-jr-engineers.slack.com/messages/CL930EVPY/) Stacks and Queues
- [#ctci-ch04](https://linkedin-jr-engineers.slack.com/messages/CL0HVSS49/) Trees and Graphs
- [#ctci-ch08](https://linkedin-jr-engineers.slack.com/messages/CMY2R0VBK/) Recursion and Dynamic Programming

- Use the [#pair-programming](https://linkedin-jr-engineers.slack.com/messages/CL6UDFVSR/) channel to ask for help or offer to work together with others.
- Please [#introduce-yourself](https://linkedin-jr-engineers.slack.com/messages/CDG6ZSWMU/) and talk about your [#job-search](https://linkedin-jr-engineers.slack.com/messages/CDE3RK8QY/). Don't use the [#general](https://linkedin-jr-engineers.slack.com/messages/CDDPLUHQC/) channel to introduce yourself.
- Our [#eloquentjavascript](https://linkedin-jr-engineers.slack.com/messages/CDD6ZFLTS/) channel discusses that book.

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

Since I'm don't want to type all these lines, I added these lines to my [`.bash_profile`](https://natelandau.com/my-mac-osx-bash_profile/):

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

In the future, as I add new code to my /ctci repo, you just `cd` to YOUR /ctci fork of mine and type `gupdate`. It will automatically pull my latest code.

If you don't have a `.bash_profile`, create this file in your home directory. After editing it, run the file by doing [`source ~/.bash_profile`](https://stackoverflow.com/questions/4608187/how-to-reload-bash-profile-from-the-command-line).

By Raymond Gan
