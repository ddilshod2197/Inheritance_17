# 17. Sport musobaqasi

class Competitor:
    def __init__(self, name, score):
        self.name = name
        self.score = score          # ball (masalan 0–100 yoki vaqtga qarab)

    def get_result(self):
        """Ishtirokchining natijasi (ball)"""
        return self.score

    def __str__(self):
        return f"{self.name:12} | Ball: {self.score:5}"


# -----------------------------------------------
# Voris sinflar (turga mos format va emoji)
# -----------------------------------------------

class Runner(Competitor):
    def get_result(self):
        return self.score

    def __str__(self):
        return f"🏃 {self.name:10} → natija: {self.score:3} ball"


class Swimmer(Competitor):
    def get_result(self):
        return self.score

    def __str__(self):
        return f"🏊 {self.name:10} → natija: {self.score:3} ball"


# --------------------------------------------------
# Musobaqa natijalarini chiqarish
# --------------------------------------------------

def show_competition_results(participants):
    print("\n" + "═" * 55)
    print("     SPORT MUSOBAQASI — NATIJALAR JADVALI     ".center(55))
    print("═" * 55)
    print("Ishtirokchi          Natija (ball)")
    print("─" * 55)

    sorted_participants = sorted(participants, key=lambda x: x.get_result(), reverse=True)

    for i, p in enumerate(sorted_participants, 1):
        medal = ""
        if i == 1:
            medal = " 🥇"
        elif i == 2:
            medal = " 🥈"
        elif i == 3:
            medal = " 🥉"
        
        print(f"{i:2}. {p}{medal}")

    print("─" * 55)
    
    if participants:
        best = max(participants, key=lambda x: x.get_result())
        print(f"Eng yaxshi natija: {best.name} — {best.get_result()} ball")
    
    print("═" * 55 + "\n")


# Test ma'lumotlari
ishtirokchilar = [
    Runner("Ali", 85),
    Swimmer("Vali", 92),
    Runner("Sardor", 78),
    Swimmer("Nodira", 88),
    Runner("Zilola", 91),
    Swimmer("Jamshid", 79),
]

show_competition_results(ishtirokchilar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol ishtirokchilaringiz:\n")
misol_ishtirokchilar = [
    Runner("Ali", 85),
    Swimmer("Vali", 90),
]

show_competition_results(misol_ishtirokchilar)
