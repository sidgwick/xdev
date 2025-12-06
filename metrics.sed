#!/usr/bin/env sed -f

/expr":/{
    s/pod_name=....pod_name../pod_name=~\\"$pod_name\\",uri=~\\"$uri\\"/g
}
