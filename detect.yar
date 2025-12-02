rule SUS {
    meta:
        description = "sus actions"
        author = "Security"
        severity = "High"
        date = "2025-12-02"
    
    strings:
        $exec_require = "require('child_process')" ascii
        $exec_func    = "exec(" ascii
        $spawn_func   = "spawn(" ascii
        $rev_tcp      = "/dev/tcp/" ascii
        $rev_bash     = "/bin/bash" ascii
        $rev_sh       = "/bin/sh" ascii        
        $rev_cmd      = "cmd.exe" ascii
        $env_steal    = "process.env" ascii
        $net_http     = "http.request" ascii
        $net_socket   = "net.Socket" ascii
        $susp_port    = /[:\s,](4444|8080|9001|1337|6666|9999)/
    condition:
        (
            ($exec_require or $exec_func or $spawn_func) and 
            ($rev_tcp or $rev_bash or $rev_sh or $rev_cmd)
        )
        or
        (
            $env_steal and 
            ($net_http or $net_socket) and 
            ($exec_func or $spawn_func)
        )
        or
        (
            ($exec_require or $exec_func or $spawn_func) and 
            $susp_port
        )
}
