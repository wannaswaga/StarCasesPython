// Функция для открытия кейса и обновления баланса
function openCase(price) {
  const balanceElement = document.getElementById("balanceAmount");
  let currentBalance = parseInt(balanceElement.innerText);

  if (currentBalance >= price) {
    // Логика открытия кейса
    currentBalance -= price;
    balanceElement.innerText = currentBalance;

    // Эффект открытия кейса
    alert(`Вы открыли кейс за ${price} ⭐!`);

    // Обновление и отображение результата
    setTimeout(() => {
      alert("Ваш приз: 150 ⭐");
      currentBalance += 150; // Пример награды
      balanceElement.innerText = currentBalance;
    }, 1000);
  } else {
    alert("Недостаточно звезд для открытия этого кейса.");
  }
}

// Функция для открытия страницы с настройками
function openSettings() {
  alert("Здесь будет страница с пополнением, выводом и историей.");
}

// Функция для перехода на главную страницу (логотип)
function goToHomePage() {
  location.reload();
}

// Инициализация Telegram Web App
Telegram.WebApp.ready();
