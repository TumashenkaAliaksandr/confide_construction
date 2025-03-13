let currentStep = 1;

function nextStep(next) {
    // Проверяем, находимся ли мы на шаге 2
    if (currentStep === 2) {
        const selectedProjectType = document.querySelector('input[name="project_type"]:checked');
        if (!selectedProjectType) {
            alert('Please select a project type (A single project or A variety of projects).'); // Сообщение пользователю
            return; // Прерываем выполнение функции, если тип проекта не выбран
        }
    }

    // Проверяем, находимся ли мы на шаге 3
    if (currentStep === 3) {
        const singleProjectOptions = document.getElementById('single-project-options');
        const varietyProjectOptions = document.getElementById('variety-project-options');

        // Проверяем, если выбран тип проекта "A single project"
        if (singleProjectOptions.style.display === 'block') {
            const selectedRadio = document.querySelector('input[name="subcategory"]:checked');
            if (!selectedRadio) {
                alert('Please select a subcategory for a single project.'); // Сообщение пользователю
                return; // Прерываем выполнение функции
            }
        }

        // Проверяем, если выбран тип проекта "A variety of projects"
        if (varietyProjectOptions.style.display === 'block') {
            const selectedCheckboxes = document.querySelectorAll('input[name="subcategories"]:checked');
            if (selectedCheckboxes.length === 0) {
                alert('Please select at least one subcategory for a variety of projects.'); // Сообщение пользователю
                return; // Прерываем выполнение функции
            }
        }
    }

    // Проверяем, находимся ли мы на шаге 4
    if (currentStep === 4) {
        const selectedLocationType = document.querySelector('input[name="location_type"]:checked');
        if (!selectedLocationType) {
            alert('Please select a location type (Home or Business).'); // Сообщение пользователю
            return; // Прерываем выполнение функции, если тип местоположения не выбран
        }
    }

    // Проверяем, находимся ли мы на шаге 5
    if (currentStep === 5) {
        const selectedDate = document.querySelector('input[name="date"]:checked');
        if (!selectedDate) {
            alert('Please select a date for your project.'); // Сообщение пользователю
            return; // Прерываем выполнение функции, если дата не выбрана
        }
    }

    // Проверяем, находимся ли мы на шаге 6
    if (currentStep === 6) {
        const selectedTime = document.querySelector('input[name="time"]:checked');
        if (!selectedTime) {
            alert('Please select a time for your project.'); // Сообщение пользователю
            return; // Прерываем выполнение функции, если время не выбрано
        }
    }

    // Убираем активный класс у всех шагов
    $('.step').removeClass('active');
    // Добавляем активный класс к следующему шагу
    $(`#step${next}`).addClass('active');
    // Обновляем текущий шаг
    currentStep = next;
}

function prevStep(prev) {
    $('.step').removeClass('active'); // Убираем активный класс у всех шагов
    $(`#step${prev}`).addClass('active'); // Добавляем активный класс к предыдущему шагу
    currentStep = prev; // Обновляем текущий шаг
}

$(document).ready(function () {
    $('#orderForm').submit(function (e) {
        e.preventDefault();

        // Валидация последнего шага (Шаг 7)
        if (currentStep !== 7) return;

        $.ajax({
            url: "{% url 'webapp:order_view' %}",
            method: "POST",
            data: new FormData(this),
            processData: false,
            contentType: false,
            success: function (response) {
                alert('Заявка успешно отправлена!');
                window.location.reload();
            },
            error: function (xhr) {
                alert('Ошибка: ' + xhr.responseJSON.error);
            }
        });
    });

    // Получаем элементы второго шага
    const projectTypeRadios = document.querySelectorAll('input[name="project_type"]');

    // Получаем контейнеры третьего шага
    const singleProjectOptions = document.getElementById('single-project-options');
    const varietyProjectOptions = document.getElementById('variety-project-options');

    // Слушаем изменения на втором шаге
    projectTypeRadios.forEach(radio => {
        radio.addEventListener('change', function () {
            if (this.value === 'single_project') {
                // Показываем радиокнопки и скрываем чекбоксы
                singleProjectOptions.style.display = 'block';
                varietyProjectOptions.style.display = 'none';
            } else if (this.value === 'variety_of_projects') {
                // Показываем чекбоксы и скрываем радиокнопки
                singleProjectOptions.style.display = 'none';
                varietyProjectOptions.style.display = 'block';
            }
        });
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
