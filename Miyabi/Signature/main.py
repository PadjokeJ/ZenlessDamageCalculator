
set_bonuses = {}

combo = [1258.3, 4776.1, 4282.8]

def calculate(skillCombo):
    # vvvvvvvvvvvvv CONSTANTS vvvvvvvvvvvvv
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
    engineBase = 743
    baseAtk = baseAgentAttack + engineBase

    engineBaseCritRate = 0.24
    enginePassiveCritDamage = 0.50

    enginePassiveIcePercent = 0.40

    # vvvvvvvvvvvvv DISCS STATS vvvvvvvvvvvvv

    penRatio = 0.00
    flatPen = 0
     
    critRate = 0.00
    critDamage = 0.00

    elementBonus = 0.00

    atkPercent = 0.00
    flatAttack = 0

    # vvvvvvvvvvvvv MATHS vvvvvvvvvvvvv
    
    totalAttack = (baseAtk * (1 + atkPercent) + flatAttack) * (1 + combatAttackPercent) + combatFlatAttack
    totalCritRate = critRate + engineBaseCritRate
    totalCritDamage = enginePassiveCritDamage + critDamage
    totalIcePercent = elementBonus + enginePassiveIcePercent

    damageMult = 1 + dmgPercent + totalIcePercent

    effectiveDefense = enemyDefense * (1 - penRatio) - flatPen
    defenseMult = levelCoefficient/(levelCoefficient + max(effectiveDefense, 0))

    resistanceMult = 1 - attributeRes - allTypeRes + resReduction + resPen

    damageList = []
    for combo in skillCombo:
        baseDamage = combo * totalAttack /100.0

        damageList.append(baseDamage * damageMult * damageReductionMult * defenseMult * resistanceMult * stunMult * (1 + totalCritRate * totalCritDamage))

    return damageList

if __name__ == "__main__":
    damage = calculate(combo)
    print(damage)