document.addEventListener('DOMContentLoaded', function () {
    // Получаем элементы DOM
    const zipCodeInput = document.querySelector('input[name="zip_code"]');
    const regionInfo = document.getElementById('regionInfo');
    const locationIcon = document.querySelector('.location-icon');

    // Проверяем наличие элементов
    if (!zipCodeInput || !regionInfo || !locationIcon) {
        console.warn('Не найдены необходимые элементы на странице.');
        return;
    }

    // Функция для обновления информации о регионе
    function updateRegionInfo(zipCode) {
        if (zipCode.length === 5) {
            fetch(`https://api.zippopotam.us/us/${zipCode}`)
                .then(response => response.json())
                .then(data => {
                    if (data && data.places && data.places.length > 0) {
                        const place = data.places[0];
                        regionInfo.innerText = `${place.state} - ${place["place name"]}`;
                    } else {
                        regionInfo.innerText = '';
                    }
                })
                .catch(error => {
                    console.error('Ошибка при получении информации о регионе:', error);
                    regionInfo.innerText = '';
                });
        } else {
            regionInfo.innerText = '';
        }
    }

    // Слушаем изменения в поле зип-кода
    zipCodeInput.addEventListener('input', function () {
        const zipCode = this.value.trim();
        updateRegionInfo(zipCode);
    });

    // Функция для обработки геолокации
    function handleGeolocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success, error);
        } else {
            alert('Ваш браузер не поддерживает геолокацию.');
        }
    }

    // Слушаем клик на иконке
    locationIcon.addEventListener('click', handleGeolocation);

    function success(position) {
        const { latitude, longitude } = position.coords;

        // Функция для обработки данных геолокации
        function handleGeolocationData(data) {
            if (data.address && data.address.postcode) {
                zipCodeInput.value = data.address.postcode;
                updateRegionInfo(data.address.postcode);
            } else {
                alert('Не удалось определить зип-код по вашему местоположению.');
            }
        }

        // Функция для обработки ошибок геолокации
        function handleGeolocationError(error) {
            console.error('Ошибка при получении данных геолокации:', error);
            alert('Не удалось определить ваше местоположение.');
        }

        // Получаем данные геолокации
        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&zoom=18&addressdetails=1`)
            .then(response => response.json())
            .then(handleGeolocationData)
            .catch(handleGeolocationError);
    }

    function error() {
        alert('Не удалось определить ваше местоположение.');
    }

    // Валидация формы, переходы между шагами и отправка формы
    let currentStep = 1;

    // Функция для проверки всех шагов перед отправкой формы
    function validateAllSteps() {
        for (let step = 1; step <= currentStep; step++) {
            if (!validateStep(step)) {
                alert(`Please complete step ${step} before proceeding.`);
                return false;
            }
        }
        return true;
    }

    // Валидация текущего шага
    function validateStep(step) {
        switch (step) {
            case 1:
                if (!zipCodeInput || !/^\d{5}$/.test(zipCodeInput.value.trim())) {
                    alert('Please enter a valid 5-digit ZIP code.');
                    return false;
                }
                break;

            case 2:
                if (!document.querySelector('input[name="project_type"]:checked')) {
                    alert('Please select a project type.');
                    return false;
                }
                break;

            case 3:
            const singleProject = document.getElementById('single-project-options');
            const varietyProject = document.getElementById('variety-project-options');

            if (singleProject && singleProject.style.display === 'block' && !document.querySelector('input[name="subcategory"]:checked')) {
                alert('Please select a subcategory.');
                return false;
            }
            if (varietyProject && varietyProject.style.display === 'block' && document.querySelectorAll('input[name="subcategories"]:checked').length === 0) {
                alert('Please select at least one subcategory.');
                return false;
            }
            break;

            case 4:
                if (!document.querySelector('input[name="location_type"]:checked')) {
                    alert('Please select a location type.');
                    return false;
                }
                break;

            case 5:
                if (!document.querySelector('input[name="timeframe"]:checked')) {
                    alert('Please select a timeframe.');
                    return false;
                }
                break;

            case 6:
                if (!document.querySelector('input[name="time"]:checked')) {
                    alert('Please select a time.');
                    return false;
                }
                break;

            case 7:
                const email = document.getElementById('email');
                const phone = document.getElementById('phone');
                const name = document.getElementById('name');

                if (!email || !phone || !name) {
                    alert('Please fill all contact fields.');
                    return false;
                }

                if (!name.value || !phone.value || !email.value) {
                    alert('Please fill all contact fields.');
                    return false;
                }

                if (!/^\+1\d{10}$/.test(phone.value.replace(/[^0-9\+]/g, ''))) {
                    alert('Please enter a valid U.S. phone number starting with +1.');
                    return false;
                }

                if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email.value)) {
                    alert('Please enter a valid email.');
                    return false;
                }
                break;

            case 8:
                const photoInputs = document.querySelectorAll('#photo-upload-section input[type="file"]');
                let hasFiles = false;

                photoInputs.forEach(input => {
                    if (input.files.length > 0) {
                        hasFiles = true;
                    }
                });

                if (!hasFiles) {
                    alert('Please upload at least one photo.');
                    return false;
                }

                if (photoInputs.length > 5) {
                    alert('Maximum 5 photos allowed.');
                    return false;
                }
                break;


            case 9: // Шаг 9 - Описание работы
                const jobDescription = document.getElementById('job_description');

                if (!jobDescription || !jobDescription.value.trim()) {
                    alert('Please provide a description of the work.');
                    return false;
                }
                break;

            case 10: // Шаг 10 - Количество часов
                const hoursNeeded = document.getElementById('hours_needed');

                if (!hoursNeeded || !hoursNeeded.value.trim()) {
                    alert('Please specify the estimated number of hours.');
                    return false;
                }

                if (isNaN(hoursNeeded.value) || Number(hoursNeeded.value) <= 0) {
                    alert('Please enter a valid number of hours greater than 0.');
                    return false;
                }
                break;

            case 11: // Шаг 11 - Дата и время визита
                const appointmentDate = document.getElementById('appointment_date');
                const appointmentTime = document.getElementById('appointment_time');

                if (!appointmentDate || !appointmentDate.value.trim()) {
                    alert('Please select an appointment date.');
                    return false;
                }

                if (!appointmentTime || !appointmentTime.value.trim()) {
                    alert('Please select an appointment time.');
                    return false;
                }

                // Проверяем, чтобы дата не была в прошлом
                const selectedDate = new Date(appointmentDate.value);
                const currentDate = new Date();
                currentDate.setHours(0, 0, 0, 0); // Убираем время для сравнения только по дате

                if (selectedDate < currentDate) {
                    alert('The appointment date cannot be in the past.');
                    return false;
                }
                break;

            default:
                return true;
        }
        return true;
    }

    // Переход к следующему шагу
    window.nextStep = function (next) {
        if (!validateStep(currentStep)) return;

        document.querySelectorAll('.step').forEach(step => step.classList.remove('active'));
        document.querySelector(`#step${next}`).classList.add('active');

        currentStep = next;
        updateStepIndicator();
    }

    // Переход к предыдущему шагу
    window.prevStep = function (prev) {
        document.querySelectorAll('.step').forEach(step => step.classList.remove('active'));
        document.querySelector(`#step${prev}`).classList.add('active');

        currentStep = prev;
        updateStepIndicator();
    }

    // Обновление индикатора текущего шага
    function updateStepIndicator() {
        document.querySelectorAll('.step-indicator').forEach((indicator, index) => {
            indicator.classList.toggle('active', index + 1 === currentStep);
        });
    }

    // Инициализация проекта
    const projectTypeRadios = document.querySelectorAll('input[name="project_type"]');
    const singleProjectOptions = document.getElementById('single-project-options');
    const varietyProjectOptions = document.getElementById('variety-project-options');

    projectTypeRadios.forEach(radio => {
        radio.addEventListener('change', () => {
            const isSingleProject = radio.value === 'single_project';

            singleProjectOptions.style.display = isSingleProject ? 'block' : 'none';
            varietyProjectOptions.style.display = !isSingleProject ? 'block' : 'none';

            // Удаляем атрибут required у скрытых элементов
            document.querySelectorAll('input[name="subcategory"]').forEach(input => input.required = isSingleProject);
            document.querySelectorAll('input[name="subcategories"]').forEach(input => input.required = !isSingleProject);
        });
    });

    // Обработка отправки формы
    $('#orderForm').submit(function (e) {
        e.preventDefault();

        if (!validateAllSteps()) return;

        // Выводим URL в скрытый input для использования в JavaScript
        const orderUrl = document.getElementById('orderUrl').value;
        const myAccountUrl = document.getElementById('myAccountUrl').value;

        const formData = new FormData(this);

        $.ajax({
            url: orderUrl,
            method: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                alert("Request submitted successfully!");
                window.location.href = myAccountUrl;
            },
            error: function (xhr) {
                alert("Error: " + (xhr.responseJSON?.error || "Server error"));
                prevStep(currentStep); // Возвращаем пользователя на последний шаг
            }
        });
    });

    // Автоматическое форматирование телефона
    $('#phone').on("input", function () {
        let value = $(this).val().replace(/[^0-9\+]/g, '');
        $(this).val(value.slice(0, 12)); // Ограничиваем длину до 12 символов (+1 и 10 цифр)
    });

    // Инициализация выбранного типа проекта при загрузке страницы
    const selectedType = document.querySelector('input[name="project_type"]:checked');
    if (selectedType && selectedType.value === "single_project") singleProjectOptions.style.display = "block";
});
