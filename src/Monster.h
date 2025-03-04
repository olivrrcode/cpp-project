#ifndef MONSTER_H
#define MONSTER_H

class Monster
{
public:
    Monster();
    bool isAlive() const;
    int attack();
    void takeDamage(int damage);

private:
    int health;
    int attackPoints;
};

#endif // MONSTER_H
