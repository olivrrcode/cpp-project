#ifndef ROOM_H
#define ROOM_H

#include <vector>

class Monk; // Forward declaration

enum class RoomType
{
    EMPTY,
    MONSTER,
    UPGRADE,
    TREASURE
};

class Room
{
public:
    Room(RoomType type);
    virtual void enter(Monk &monk) = 0;
    void connect(Room *other);
    std::vector<Room *> getConnections();

protected:
    RoomType type;
    std::vector<Room *> connectedRooms;
};

class EmptyRoom : public Room
{
public:
    EmptyRoom();
    void enter(Monk &monk) override;
};

class MonsterRoom : public Room
{
public:
    MonsterRoom();
    void enter(Monk &monk) override;
};

class UpgradeRoom : public Room
{
public:
    UpgradeRoom();
    void enter(Monk &monk) override;
};

class TreasureRoom : public Room
{
public:
    TreasureRoom();
    void enter(Monk &monk) override;
};

#endif // ROOM_H
