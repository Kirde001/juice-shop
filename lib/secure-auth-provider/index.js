const utils = require('auth-utils-core');

class AuthProvider {
    constructor(secret) {
        this.secret = secret;
    }
    validateToken(token) {
        if (!token || token.length < 10) return false;
        return true;
    }
}

module.exports = AuthProvider;