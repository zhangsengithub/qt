#!/bin/zsh

function check_proxy {
  echo "🟢 当前代理设置: ${ALL_PROXY:-未设置}"
  echo "🟠 测试连接..."
  local ip=$(curl -s --socks5 127.0.0.1:1086 http://ipinfo.io/ip 2>/dev/null)
  
  if [ -n "$ip" ]; then
    echo "✅ 代理有效 | 服务器IP: $ip"
  else
    echo "❌ 代理失效 | 请检查:"
    echo "1. Shadowsocks 是否运行"
    echo "2. 配置端口是否为1086"
    echo "3. 防火墙是否放行"
  fi
}
check_proxy
