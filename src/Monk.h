#ifndef MONK_H
#define MONK_H

#include <string>

class Room; // Forward declaration

class Monk
{
public:
    Monk(std::string name);
    void moveTo(Room *nextRoom);
    void meditate();
    void upgradeHealth();
    void upgradeAttack();
    bool isAlive() const;
    int getHealth() const;
    int getAttack() const;

private:
    std::string name;
    int health;
    int attack;
    Room *currentRoom;
};

#endif // MONK_H
