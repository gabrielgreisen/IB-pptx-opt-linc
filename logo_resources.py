import os
from brandfetcher import get_brandfetch_logo, download_logo_file

def ensure_logo_available(logo_name, domain, logo_base_dir="logos"):
    """
    Checks if the logo PNG exists in the local logos folder.
    If not, attempts to fetch it from Brandfetch using the domain
    and saves it under logo_name.

    Parameters
    ----------
    logo_name : str
        The cleaned name to use for the local PNG file (without .png).

    domain : str
        The company website domain (like 'afya.com.br') to use for Brandfetch.

    logo_base_dir : str
        Directory where logo PNG files are stored.

    Returns
    -------
    str or None
        The full path to the logo file if it exists or was fetched successfully, else None.
    """

    logo_file = os.path.join(logo_base_dir, f"{logo_name}.png")
    if os.path.exists(logo_file):
        return logo_file
    else:
        print(f"🔍 Attempting to fetch logo for {domain} to save as {logo_name}")
        logo_url = get_brandfetch_logo(domain)
        if logo_url:
            download_logo_file(logo_url, logo_name, save_dir=logo_base_dir)
            if os.path.exists(logo_file):
                print(f"✅ Successfully fetched and saved logo for {domain}")
                return logo_file
        print(f"✅ Successfully fetched and saved logo for {domain}")
        return None