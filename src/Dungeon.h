#ifndef DUNGEON_H
#define DUNGEON_H

#include <vector>
#include "Room.h"

class Dungeon
{
public:
    Dungeon();
    void generateDungeon();
    Room *getStartingRoom();

private:
    std::vector<Room *> rooms;
};

#endif // DUNGEON_H
