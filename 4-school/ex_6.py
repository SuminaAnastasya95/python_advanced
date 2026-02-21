

from dataclasses import dataclass, field


@dataclass
class Student:
    """Формирование студентов"""
    name: str
    lesson_data: dict[str, list[int]] = field(default_factory=dict)


class Calculates:
    """Расчет средних баллов по предмету"""

    def get_avg_for_subject(self, grades: list[int]):
        return sum(grades) / len(grades) if grades else 0

    def get_total_avg(self, student: Student):
        all_grades = []
        for grades in student.lesson_data.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0


class Monitoring:
    def check_student(self, calculate: Calculates, student: Student):
        total_avg = calculate.get_total_avg(student)
        problem_lesson = [name for name, grades in student.lesson_data.items()
                          if calculate.get_avg_for_subject(grades) < 3.5]
        return {
            "name": student.name,
            "total": total_avg,
            "problems": problem_lesson,
            "is_critical": total_avg < 3.5 or len(problem_lesson) > 0
        }


class Notification:
    """Уведомления"""

    def notification_warning(self, report: dict):
        if report["is_critical"]:
            print(f"⚠️ ВНИМАНИЕ: У студента {report['name']} проблемы!")
            print(f"   Общий балл: {report['total']:.2f}")
            if report["problems"]:
                print(f"   Нужно подтянуть: {', '.join(report['problems'])}")
        else:
            print(f"✅ У студента {report['name']} всё в порядке.")


vasia = Student("Вася", {
    "Математика": [2, 3, 3],  # средний 2.6
    "Физика": [5, 5, 4]      # средний 4.6
})

# 2. Инициализация сервисов
calc = Calculates()
monitor = Monitoring()
notify = Notification()

# 3. Процесс
status = monitor.check_student(calc, vasia)
notify.notification_warning(status)
