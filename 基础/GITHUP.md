### githup修改过的文件上传到远程
**1.git status**
查看状态
**2.git stash**
备份当前的工作区的内容，从最近的一次提交中读取相关内容，让工作区保证和上次提交的内容一致。同时，将当前的工作区内容保存到Git栈中
**3.git pull**
拉取服务器上的内容
**4.git stash pop**
从Git栈中读取最近一次保存的内容，恢复工作区的相关内容
**5.git push -u origin gh-pages**
提交至远程
### 切换分支
**git branch -a**
查看分支
**git checkout gh-pages**