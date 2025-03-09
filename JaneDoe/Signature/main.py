# vvvvvvvvvvvvv CONSTANTS vvvvvvvvvvvvv
combo = [1266.20, 209.00, 602.20, 323.00, 1150.00, 1150.00, 0, 209.00, 2941.30, 0]

level = 60
levelCoefficient = 794
    
enemyDefense = 600
stunMult = 2

attributeRes = 0
allTypeRes = 0
resReduction = 0
resPen = 0

dmgPercent = 0
damageReductionMult = 1

combatAttackPercent = 0.00
combatFlatAttack = 0

baseAgentAttack = 805 + 75
engineBase = 713
baseAtk = baseAgentAttack + engineBase

baseAnomalyMastery = 36
anomalyPercent = 1

anomalyMultipliers = {
    "Burn": 0.50 * 20,
    "Shock": 1.25 * 10,
    "Corruption": 0.625 * 20,
    "Shatter": 5.00, 
    "Assault": 7.13,
    "Flinch": 7.13,
}

# vvvvvvvvvvvvv DISCS STATS vvvvvvvvvvvvv

penRatio = 0.00
flatPen = 0
    
critRate = 0.00
critDamage = 0.00

elementBonus = 0.00

atkPercent = 0.00
flatAttack = 0

anomalyProficiency = 0

# vvvvvvvvvvvvv MATHS vvvvvvvvvvvvv

def janeDoe_combo(skillCombo):

    totalCritRate = critRate + 0.05
    totalCritDamage = critDamage + 0.50
    totalAttack = (baseAtk * (1 + atkPercent) + flatAttack) * (1 + combatAttackPercent) + combatFlatAttack

    damageMult = 1 + dmgPercent + elementBonus
    
    effectiveDefense = enemyDefense * (1 - penRatio) - flatPen
    defenseMult = levelCoefficient/(levelCoefficient + max(effectiveDefense, 0))

    resistanceMult = 1 - attributeRes - allTypeRes + resReduction + resPen

    damageList = []
    for combo in skillCombo:
        baseDamage = combo * totalAttack /100.0

        damageList.append(baseDamage * damageMult * damageReductionMult * defenseMult * resistanceMult * stunMult * (1 + totalCritRate * totalCritDamage))

    return damageList

def janeDoe_assault():
    bonusAttack = min(
        (max(120, anomalyProficiency) - 120) * 2,
        600)

    passiveCritRate = 0.16 * anomalyProficiency

    assaultCritRate = 0.40 + passiveCritRate
    assaultCritDamage = 0.50

    totalAttack = (baseAtk * (1 + atkPercent) + flatAttack) + bonusAttack

    baseDamage = anomalyMultipliers["Flinch"] * totalAttack

    effectiveDefense = enemyDefense * (1 - penRatio) - flatPen
    defenseMult = levelCoefficient/(levelCoefficient + max(effectiveDefense, 0))

    resistanceMult = 1 - attributeRes - allTypeRes + resReduction + resPen
    stunMult = 2

    APMult = anomalyProficiency / 100

    buffLevelMultiplier = 1 + (level - 1) / 59.0

    return baseDamage * anomalyPercent * defenseMult * resistanceMult * stunMult * APMult * buffLevelMultiplier * (1 + assaultCritRate * assaultCritDamage)

def calculate(combo):

    damage = janeDoe_combo(combo)
    assault = janeDoe_assault()

    damageList = []
    for hit in damage:
        damageList.append(hit)
    
    damageList.append(assault)
    damageList.append(assault)

    return damageList

if __name__ == "__main__":
    damage = calculate(combo)
    print(damage)