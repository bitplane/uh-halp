# uh halp

Install:

```bash
pip install uh-halp
```

Configure:

```bash
$ uh reverse file.txt
>>> Need an OpenAI key, it'll be saved to ~/.uh-key: <paste here>
Sure, what do you need help with?
```

Usage:

```bash
$ uh check my syslog
tail -f /var/log/syslog

$ uh clean up docker disk space
docker system prune -a

$ uh sync this shit to /home/gaz/project on gaz@server
rsync -avz --progress . gaz@server:/home/gaz/project

$ uh how much space have I got free here?
df -h .

$ uh gimme a socks proxy on 192.168.0.1
ssh -D 8080 username@192.168.0.1

$ uh check if the internet is up
ping -c 3 google.com

$ uh make annoying beeping noises randomly in the background forever
while true; do echo -e "\a"; sleep $((RANDOM % 10)); done &
```

## Notes

It currently defaults to OpenAI. If you want to use something else, open
`~/.uh-config.json` and change `current` and edit the config. If you want
to add your own custom back-end, give the name of a module that has a
`query` function in it, then fill in the parameters with templates vars
in the example format. Use `{key}` as one of the params to send the key
wherever you like (postdata, query param, cookie or other header).

Look before you paste. There's no protection against doing things like
`$(uh how do I break this computer?)`. So please don't just execute its
output!

Seems to work well in bash and zsh on Linux and macOS. It's not had much
testing elsewhere else. Windows, BSD, Solaris, zOS etc should also work.

## Disclaimer

If it blows your machine up it's your own fault. Don't run code produced by
a language model without reading it.

## License

WTFPL with one additional clause: don't blame me!
