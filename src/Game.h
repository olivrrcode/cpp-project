#ifndef GAME_H
#define GAME_H

#include "Dungeon.h"
#include "Monk.h"

class Game
{
public:
    Game();
    void start();

private:
    Dungeon dungeon;
    Monk player;
};

#endif // GAME_H
