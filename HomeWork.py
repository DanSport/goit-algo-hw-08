import heapq

def merge_cables(cables):
    # Ініціалізуємо купу
    heapq.heapify(cables)
    
    # Поки у купі є більше одного кабеля
    while len(cables) > 1:
        # Беремо два найкоротших кабелі
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        
        # З'єднуємо їх та додаємо новий об'єднаний кабель до купи
        total_length = shortest1 + shortest2
        heapq.heappush(cables, total_length)
    
    # Повертаємо загальну довжину кабелю
    return sum(cables)

# Приклад використання
cable_lengths = [8, 4, 6, 12, 1, 2, 3]
total_cost = merge_cables(cable_lengths)
print("Мінімальні загальні витрати на об'єднання кабелів:", total_cost)
