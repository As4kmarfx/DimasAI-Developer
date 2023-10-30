#include <iostream>
#include <chrono>
#include <thread>

void showLoadingScreen()
{
    int i = 0;
    while (i < 100)
    {
        std::cout << "Loading: " << i << "%\r";
        std::cout.flush();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        i++;
    }
    std::cout << "Loading Complete!" << std::endl;
}

int main()
{
    showLoadingScreen();
    return 0;
}
