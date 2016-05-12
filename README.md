# pyutils
pyutils

## update-hosts.py
  更新hosts 工具
  ```
  wget https://github.com/shendongming/pyutils/raw/master/update-hosts.py
  sudo python update-hosts.py
  curl https://www.google.com/ncr
  ```
  
## clean-requirements.py
  清理 pip requirements.txt 不在使用的类库
  ```  
  source project1/prj.env/bin/activate
  pip install pip_check_reqs
  
  python clean-requirements.py project1/requirements.txt project1/src
  ```
