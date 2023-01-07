const submit = document.getElementById('coin-exchange')
submit.addEventListener('click', function () {
    let alertMessage = document.getElementById('alert-messages')
    let amount = document.getElementById('amount')
    let url = '/admin/withdraw'
    let data = {'amount': amount.value, 'action': 'coin_exchange'}
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            if (data.type === 'error') {
                alertMessage.innerHTML = '<div class="alert alert-danger alert-dismissible" role="alert"> ' + data.message + '</div>'
            } else {
                let coin = document.getElementById('coin')
                let balance = document.getElementById('balance')
                coin.innerText -= amount.value
                balance.innerText = data.balance
                alertMessage.innerHTML = '<div class="alert alert-success alert-dismissible" role="alert"> ' + data.message + '</div>'
                amount.value = '';
            }
            setTimeout(function () {
                $(".alert").alert('close')
            }, 3000);
        });
})

const card_withdraw = document.getElementById('card-withdraw')
card_withdraw.addEventListener('click', function () {
    let alertMessage = document.getElementById('alert-messages')
    let amount = document.getElementById('amount1')
    let card_number = document.getElementById('card-number')
    let url = '/admin/withdraw'
    let data = {'amount': amount.value, 'card_number': card_number.value, 'action': 'card_withdraw'}
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            if (data.type === 'error') {
                alertMessage.innerHTML = '<div class="alert alert-danger alert-dismissible" role="alert"> ' + data.message + '</div>'
            } else {
                let balance = document.getElementById('balance')
                balance.innerText = data.balance
                alertMessage.innerHTML = '<div class="alert alert-success alert-dismissible" role="alert"> ' + data.message + '</div>'
                let table = document.getElementById('table')
                table.innerHTML = `<tr>
                                        <td>${data.payment.created_at}</td>
                                        <td>${data.payment.card_number}</td>
                                        <td>${data.payment.amount}</td>
                                        <td><span class="badge badge-warning">Kutilmoqda</span></td>
                                    </tr>` + table.innerHTML
                amount.value = '';
                card_number.value = '';
            }
            setTimeout(function () {
                $(".alert").alert('close')
            }, 3000);
        });
})