loginSubmit: function(t, e) {
                var n = o.Deferred(),
                    i = this;
                return this.getSaltInfo(e).done(function() {
                    t = o.extend({}, {
                        username: i.currentUid
                    }, t), c.postLogin(t, i.saltRet).done(function(t) {
                        n.resolve(t)
                    }).fail(function(t) {
                        if (t.data) {
                            var e = {};
                            t.data.require_verify_code ? (i.$contentCaptcha.is(":visible") || (i.addValidates("captcha"), i.showCaptchaNodes()), i.refreshCaptcha()) : t.data.require_device_verify ? (e = {
                                uid: t.data.uid,
                                phone_no: t.data.phone_no,
                                target: window._params.target
                            }, window.location.href = "/login/device-lock?" + p.transformRequest(e)) : t.data.require_phone_bind && (e = {
                                uid: t.data.uid,
                                target: window._params.target
                            }, window.location.href = "/login/device-phone?" + p.transformRequest(e))
                        }
                        n.reject(t)
                    })
                }).fail(function(t) {
                    n.reject(t)
                }), n
            },


function(t, e, n) {
    var i,
        r,
        a = n(2),
        o = n(19),
        s = n(22),
        u = n(117),
        l = n(115);
    i = [], r = function() {
        return {
            getSalt: function(t) {
                var e = a.Deferred();
                return t.account = a.trim(t.account), o.get({
                    url: "/login/salt",
                    data: a.extend({}, {
                        device_id: s.get()
                    }, t),
                    timeout: 1e4
                }).done(function(t) {
                    e.resolve(t)
                }).fail(function(t) {
                    e.reject(t)
                }), e
            },
            postLogin: function(t, e) {
                var n = a.Deferred(),
                    i = e.tgtgt_params;
                i.salt = e.svr_result.salt;
                var r = u.get(t.password, i);
                return delete t.password, t.rememberMe = t.autologin, t.username = a.trim(t.username), o.post({
                    url: "/auth/login",
                    data: a.extend({}, {
                        device_id: s.get(),
                        tgtgt: r
                    }, t),
                    timeout: 1e4
                }).done(function(t) {
                    n.resolve(t)
                }).fail(function(t) {
                    t && 403 === +t.result && (t.ret_msg = l.errorForbidLogin), n.reject(t)
                }), n
            }
        }
    }.apply(e, i), !(void 0 !== r && (t.exports = r))
}

https://passport.futu5.com/login/salt?device_id=1529634044507277&account=rockgarden%40sina.com&_=1529635695456

response:
{
"code": 0,
"message": "",
"data": {
"svr_result": {
"require_verify_code": "false",
"salt": "N&sJ$%H4b%IeKLyD",
"svr_time": 1529636187,
"uid": 294152
},
"tgtgt_params": {
"ver": 1,
"uid": 294152,
"init_time": 1529636187,
"refresh_time": 1529636187,
"invalid_time": 1532228187,
"os_type": 15,
"seq": 0,
"signed_len": 0,
"signed": ""
}
}
}

Request URL: https://passport.futu5.com/auth/login
Request Method: POST
Status Code: 200 OK
Remote Address: 119.29.47.198:443
Referrer Policy: no-referrer-when-downgrade

device_id: 1529634044507277
tgtgt: gpKXLveX203e0J%2BGC0w0Ovoez2X1yV3M6ygEm0%2BJ%2BMhOfSBGbUwllC3Jqxq5stJTsHvRsNQ0yjufcH%2Fs8wEhlJdA0UZZlV3B7Ug84NPodjNkd0Rnh%2BxbRqL8hcwDp%2FMpHlsxfcaWjhSWiVkZPpEagA%3D%3D
username: 294152    
code: %2B852
phone: 
email: rockgarden%40sina.com
captcha: 
domain: futu5.com%0D%0A++++++++++++
device_type: web
_csrf-frontend: eThDSElTLlQmXyoqLwtbJTAIMB05KUBsMX0JDg0%2FGmADABc6DRJtDQ%3D%3D

source
device_id=1529634044507277&tgtgt=gpKXLveX203e0J%2BGC0w0Ovoez2X1yV3M6ygEm0%2BJ%2BMhOfSBGbUwllC3Jqxq5stJTsHvRsNQ0yjufcH%2Fs8wEhlJdA0UZZlV3B7Ug84NPodjNkd0Rnh%2BxbRqL8hcwDp%2FMpHlsxfcaWjhSWiVkZPpEagA%3D%3D&username=294152&code=%2B852&phone=&email=rockgarden%40sina.com&captcha=&domain=futu5.com%0D%0A++++++++++++&device_type=web&_csrf-frontend=eThDSElTLlQmXyoqLwtbJTAIMB05KUBsMX0JDg0%2FGmADABc6DRJtDQ%3D%3D