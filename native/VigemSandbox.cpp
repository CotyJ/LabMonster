#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <Xinput.h>
#include "ViGemClient.h"
#include <iostream>
#include <thread>
#include <chrono>
#pragma comment(lib, "setupapi.lib")
#pragma comment(lib, "Xinput.lib")


int main() {
    // To initialize the API call vigem_alloc which gives you an opaque handle to the underlying driver:
    const auto client = vigem_alloc();
    if (client == nullptr)
    {
        std::cerr << "Uh, not enough memory to do that?!" << std::endl;
        return -1;
    }

    // Establish connection to the driver
    const auto vsuccess_val = vigem_connect(client);
    if (!VIGEM_SUCCESS(vsuccess_val))
    {
        std::cerr << "ViGEm Bus connection failed with error code: 0x" << std::hex << vsuccess_val << std::endl;
        return -1;
    }

    // Allocate handle to identify new pad
    const auto pad = vigem_target_x360_alloc();

    // Add client to the bus, this equals a plug-in event
    const auto pir = vigem_target_add(client, pad);

    std::cout << "Connecting..." << std::endl;

    // Error handling
    if (!VIGEM_SUCCESS(pir))
    {
        std::cerr << "Target plugin failed with error code: 0x" << std::hex << pir << std::endl;
        vigem_target_free(pad);
        return -1;
    }

    // ~~~ Controller is now registered and available ~~~
    std::cout << "X360 controller created. Press enter to continue..." << std::endl;
    std::cin.get();

    // Controller state sent to Windows
    XINPUT_STATE state;
    state = {};
    std::cout << state.Gamepad.wButtons << std::endl;

    double one_frame = 1000.0 / 120.0;
    int one_int = int (one_frame);

    std::cout << "Starting in..." << std::endl;
    Sleep(500);
    std::cout << "3" << std::endl;
    Sleep(1000);
    std::cout << "2" << std::endl;
    Sleep(1000);
    std::cout << "1" << std::endl;
    Sleep(1000);
    
    int counter = 0;
    // timer for safety
    while (counter < 180) {
        // DO STUFF HERE
        std::cout << counter << ": " << state.Gamepad.wButtons << std::endl;
        // Push a button
        if (counter % 2 == 0) {
            state.Gamepad.wButtons = 0x1000;
        }
        else {
            state.Gamepad.wButtons = 0;
        }
        vigem_target_x360_update(client, pad, *reinterpret_cast<XUSB_REPORT*>(&state.Gamepad));

        // sleep one frame
        std::this_thread::sleep_for(std::chrono::milliseconds(one_int));
        counter++;
    }

    std::cout << "Finished. Press enter to cleanup..." << std::endl;
    std::cin.get();

    // Cleanup
    std::cout << "Cleaning up" << std::endl;
    vigem_target_remove(client, pad);
    vigem_target_free(pad);
    vigem_disconnect(client);
    vigem_free(client);

    std::cout << "Cleanup done" << std::endl;

    return 0;
}
