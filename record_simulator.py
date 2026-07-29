import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    os.makedirs("videos", exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # Configure context to record video, size matches a mobile screen
        context = await browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 390, "height": 844},
            viewport={"width": 390, "height": 844},
            device_scale_factor=2 # Retina quality
        )
        page = await context.new_page()
        
        # Ensure we are testing against localhost:3002
        url = "http://localhost:3002/?text=CAZZO!&emotion=angry"
        print(f"Navigating to {url}...")
        
        try:
            await page.goto(url)
            # Wait a few seconds to capture the animation
            print("Recording animation for 3 seconds...")
            await page.wait_for_timeout(3000)
        except Exception as e:
            print(f"Error accessing page: {e}. Is Next.js server running?")
        finally:
            # Closing the context actually saves the video
            await context.close()
            await browser.close()
            print("Done. Video should be saved in videos/ directory.")

if __name__ == "__main__":
    asyncio.run(main())
