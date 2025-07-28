
zhangsen

export http_proxy="127.0.0.1:8118"
export https_proxy="127.0.0.1:8118"
export ftp_proxy="127.0.0.1:8118"

ss-local -c /home/zhangsen/config/shadow.json &

curl --socks5 127.0.0.1:1086 https://ipinfo.io


{
  "local_port" : 1086,
  "timeout" : 60,
  "server_port" : 8388,
  "method" : "aes-256-cfb",
  "server" : "119.8.232.141",
  "password" : "zhangsen",
  "local_address" : "127.0.0.1"
}
