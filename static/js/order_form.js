document.addEventListener('DOMContentLoaded', function () {
    const zipCodeInput = document.querySelector('input[name="zip_code"]');
    const regionInfo = document.getElementById('regionInfo');
    const locationIcon = document.querySelector('.location-icon');

    // Функция для обновления информации о регионе
    function updateRegionInfo(zipCode) {
        if (zipCode.length === 5) {
            fetch(`https://api.zippopotam.us/us/${zipCode}`)
                .then(response => response.json())
                .then(data => {
                    if (data) {
                        const place = data.places[0];
                        regionInfo.innerText = `${place.state} - ${place["place name"]}`;
                    } else {
                        regionInfo.innerText = '';
                    }
                })
                .catch(error => console.error('Ошибка:', error));
        } else {
            regionInfo.innerText = '';
        }
    }

    // Слушаем изменения в поле зип-кода
    zipCodeInput.addEventListener('input', function () {
        const zipCode = this.value.trim();
        updateRegionInfo(zipCode);
    });

    // Слушаем клик на иконке
    locationIcon.addEventListener('click', function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success, error);
        } else {
            alert('Ваш браузер не поддерживает геолокацию.');
        }
    });

    function success(position) {
        const { latitude, longitude } = position.coords;

        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&zoom=18&addressdetails=1`)
            .then(response => response.json())
            .then(data => {
                if (data.address.postcode) {
                    zipCodeInput.value = data.address.postcode;
                    updateRegionInfo(data.address.postcode); // Обновляем информацию о регионе
                } else {
                    // Если Nominatim не вернул зип-код, используем Zippopotam для уточнения
                    fetch(`https://api.zippopotam.us/us?lat=${latitude}&lon=${longitude}`)
                        .then(response => response.json())
                        .then(data => {
                            if (data) {
                                const place = data.places[0];
                                zipCodeInput.value = place.postcode;
                                updateRegionInfo(place.postcode); // Обновляем информацию о регионе
                            } else {
                                // Если Zippopotam не вернул данные, используем Nominatim для получения региона
                                fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&zoom=18&addressdetails=1`)
                                    .then(response => response.json())
                                    .then(data => {
                                        if (data.address.state && data.address.city) {
                                            regionInfo.innerText = `${data.address.state} - ${data.address.city}`;
                                        } else {
                                            regionInfo.innerText = '';
                                        }
                                    })
                                    .catch(error => console.error('Ошибка:', error));
                            }
                        })
                        .catch(error => console.error('Ошибка:', error));
                }
            })
            .catch(error => console.error('Ошибка:', error));
    }

    function error() {
        alert('Не удалось определить ваше местоположение.');
    }
});
document.addEventListener('DOMContentLoaded', function () {
    const locationIcon = document.querySelector('.location-icon');

    locationIcon.addEventListener('click', function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success, error);
        } else {
            alert('Ваш браузер не поддерживает геолокацию.');
        }
    });

    function success(position) {
        const { latitude, longitude } = position.coords;

        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&zoom=18&addressdetails=1`)
            .then(response => response.json())
            .then(data => {
                if (data.address.postcode) {
                    const zipCodeInput = document.querySelector('input[name="zip_code"]');
                    zipCodeInput.value = data.address.postcode;

                    // Обновляем информацию о регионе
                    const regionInfo = document.getElementById('regionInfo');
                    regionInfo.innerText = `${data.address.state} - ${data.address.city}`;
                } else {
                    alert('Не удалось определить зип-код по вашему местоположению.');
                }
            })
            .catch(error => console.error('Ошибка:', error));
    }

    function error() {
        alert('Не удалось определить ваше местоположение.');
    }
})
let currentStep = 1;

// Общая функция для безопасного фокуса
function safeFocus(selector) {
    setTimeout(() => {
        const element = document.querySelector(selector);
        if (element && element.offsetParent !== null && !element.disabled) {
            element.focus();
        }
    }, 50);
}

function nextStep(next) {
    switch(currentStep) {
        case 1:
            const zipCode = document.querySelector('input[name="zip_code"]').value.trim();
            if (!/^\d{5}$/.test(zipCode)) {
                alert('Please enter a valid 5-digit ZIP code.');
                safeFocus('input[name="zip_code"]');
                return;
            }
            break;

        case 2:
            if (!document.querySelector('input[name="project_type"]:checked')) {
                alert('Please select a project type.');
                safeFocus('input[name="project_type"]');
                return;
            }
            break;

        case 3:
            const singleProject = document.getElementById('single-project-options').style.display === 'block';
            const varietyProject = document.getElementById('variety-project-options').style.display === 'block';

            if (singleProject && !document.querySelector('input[name="subcategory"]:checked')) {
                alert('Please select a subcategory.');
                safeFocus('input[name="subcategory"]');
                return;
            }
            if (varietyProject && document.querySelectorAll('input[name="subcategories"]:checked').length === 0) {
                alert('Please select at least one subcategory.');
                safeFocus('input[name="subcategories"]');
                return;
            }
            break;

        case 4:
            if (!document.querySelector('input[name="location_type"]:checked')) {
                alert('Please select a location type.');
                safeFocus('input[name="location_type"]');
                return;
            }
            break;

        case 5:
            if (!document.querySelector('input[name="timeframe"]:checked')) {
                alert('Please select a timeframe.');
                safeFocus('input[name="timeframe"]');
                return;
            }
            break;

        case 6:
            if (!document.querySelector('input[name="time"]:checked')) {
                alert('Please select a time.');
                safeFocus('input[name="time"]');
                return;
            }
            break;

        case 7:
            const email = document.getElementById('email');
            const phone = document.getElementById('phone');
            const name = document.getElementById('name');

            if (!name.value || !phone.value || !email.value) {
                alert('Please fill all contact fields.');
                if (!name.value) safeFocus('#name');
                else if (!phone.value) safeFocus('#phone');
                else safeFocus('#email');
                return;
            }

            if (!/^(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$/.test(phone.value)) {
                alert('Please enter a valid phone number.');
                safeFocus('#phone');
                return;
            }

            if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email.value)) {
                alert('Please enter a valid email.');
                safeFocus('#email');
                return;
            }
            break;

        case 8:
            const files = document.getElementById('photos').files;
            if (files.length === 0) {
                alert('Please upload at least one photo.');
                safeFocus('#photos');
                return;
            }
            if (files.length > 5) {
                alert('Maximum 5 photos allowed.');
                safeFocus('#photos');
                return;
            }
            break;
    }

    // Переход к следующему шагу
    document.querySelectorAll('.step').forEach(step => step.classList.remove('active'));
    document.querySelector(`#step${next}`).classList.add('active');
    currentStep = next;
}

function prevStep(prev) {
    document.querySelectorAll('.step').forEach(step => step.classList.remove('active'));
    document.querySelector(`#step${prev}`).classList.add('active');
    currentStep = prev;
}

$(document).ready(function() {
    // Инициализация проекта
    const projectTypeRadios = document.querySelectorAll('input[name="project_type"]');
    const singleProjectOptions = document.getElementById('single-project-options');
    const varietyProjectOptions = document.getElementById('variety-project-options');

    projectTypeRadios.forEach(radio => {
        radio.addEventListener('change', () => {
            singleProjectOptions.style.display = radio.value === 'single_project' ? 'block' : 'none';
            varietyProjectOptions.style.display = radio.value === 'variety_of_projects' ? 'block' : 'none';
        });
    });

    // Обработка отправки формы
    $('#orderForm').submit(function(e) {
        e.preventDefault();

        if (currentStep !== 8) return;

        const formData = new FormData(this);

        // Дополнительная валидация файлов
        const files = document.getElementById('photos').files;
        if (files.length > 5) {
            alert('Maximum 5 photos allowed.');
            return;
        }

        $.ajax({
            url: "{% url 'webapp:order_view' %}",
            method: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                alert('Request submitted successfully!');
                window.location.href = "{% url 'webapp:my_account' %}";
            },
            error: function(xhr) {
                alert('Error: ' + (xhr.responseJSON?.error || 'Server error'));
            }
        });
    });

    // Автоматическое форматирование телефона
    document.getElementById('phone').addEventListener('input', function(e) {
        let value = e.target.value;

        // Удаляем все нецифровые символы, кроме '+'
        value = value.replace(/[^0-9\+]/g, '');

        // Ограничиваем длину до 15 символов (учитывая '+')
        if (value.length > 15) value = value.slice(0, 15);

        e.target.value = value;
    });

    // Инициализация: проверяем выбранное значение при загрузке страницы
    const selectedType = document.querySelector('input[name="project_type"]:checked');
    if (selectedType) {
        if (selectedType.value === 'single_project') {
            singleProjectOptions.style.display = 'block';
        } else if (selectedType.value === 'variety_of_projects') {
            varietyProjectOptions.style.display = 'block';
        }
    }
});
