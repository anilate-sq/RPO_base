#include <iostream>
#include <memory>

int main(){
    auto ptr = std::make_unique<int>(67); // Создаем unique_ptr
    auto moved = std::move(ptr); // Владение передается moved, ptr == nullptr;
}

