function proxy_on() {
export ALL_PROXY="socks5://127.0.0.1:1086"
export http_proxy="http://127.0.0.1:1087"
export https_proxy="https://127.0.0.1:1087"
echo -e "终端代理已开启。"
nc -zv -X 5 -x 127.0.0.1:1086 www.google.com 443
}

function proxy_off(){
    unset http_proxy https_proxy
    echo -e "终端代理已关闭。"
}
ps -ef|grep privoxy
export http_proxy="http://127.0.0.1:1087"
export https_proxy="https://127.0.0.1:1087"
