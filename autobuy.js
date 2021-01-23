let string = '';
const ITEM = {
    "pd": 68,
    "grs": 71,
    "atb": 440,
    "brs": 74,
    "wrs": 75,
    "diamond": 67
}

const username = "yohanesyoshua"
const password = "faisal"
const passwordBank = "1111"

function beli(item_id) {
    let url = "https://seal-gladius.com/itemmall-bayarr"
    if (item_id == ITEM.atb) {
        url = "https://seal-gladius.com/itemmall-bayar"
    }
    $.ajax({
        async : false,
        url : url,
        data : {
            passbank: passwordBank,
            idmall: item_id,
            is_ajax: 1
        },
        type: "POST",
        tryCount : 0,
        retryLimit : 3,
        success: (result) => {
            //
        }
    });
}

function logout() {
    $.ajax({
        async : false,
        url : "https://seal-gladius.com/logout",
        type: "GET",
        tryCount : 0,
        retryLimit : 3,
        success: (result) => {
            //
        }
    });
}

function login() {
    const url = "https://seal-gladius.com/login"
    let data = {
        username: username,
        password: password,
        is_ajax: 1
    }

    $.ajax({
        async : false,
        url : url,
        data : data,
        type: "POST",
        tryCount : 0,
        retryLimit : 3,
        success: (result) => {
            for(let i = 0; i < 5; i++) {
                beli(ITEM.brs)
                beli(ITEM.wrs)
                beli(ITEM.diamond)
            }

            sendToDiscord("Buying 5 brs, wrs, diamond for id : **" + username + "**")

            for (let i = 0 ; i < 2 ; i++) {
                beli(ITEM.pd)
                beli(ITEM.grs)
            }

            sendToDiscord("Buying 2 pd grs for id : **" + username + "**")

            for(let i = 0; i < 40; i++) {
                beli(ITEM.atb)
            }
            sendToDiscord("Buying 40 atb for id : **" + username + "**")

            logout()
        }
    });
}

function start() {
    login()
}

function sendToDiscord(message) {
    $.ajax({
        async: false,
        url: "https://discordapp.com/api/webhooks/802486083295379467/x0D2eX1Nqk4_50ugiFGvimGVjblH6QEscfKSJca46PVIftRXA3IpgNN1o6re2VDPPrpF",
        type: "POST",
        data: {
            content: message
        }
    })
}