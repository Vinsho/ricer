class XfceTemplate:
    path = ".config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml"
    template = """<?xml version="1.0" encoding="UTF-8"?>

<channel name="xfce4-panel" version="1.0">
  <property name="configver" type="int" value="2"/>
  <property name="panels" type="array">
    <value type="int" value="1"/>
    <property name="dark-mode" type="bool" value="true"/>
    <property name="panel-1" type="empty">
      <property name="position" type="string" value="p=5;x=960;y=27"/>
      <property name="length" type="double" value="1"/>
      <property name="position-locked" type="bool" value="true"/>
      <property name="icon-size" type="uint" value="16"/>
      <property name="size" type="uint" value="27"/>
      <property name="plugin-ids" type="array">
        <value type="int" value="8"/>
        <value type="int" value="20"/>
        <value type="int" value="4"/>
        <value type="int" value="2"/>
        <value type="int" value="3"/>
        <value type="int" value="26"/>
        <value type="int" value="12"/>
        <value type="int" value="5"/>
        <value type="int" value="6"/>
        <value type="int" value="1"/>
        <value type="int" value="22"/>
        <value type="int" value="9"/>
        <value type="int" value="10"/>
        <value type="int" value="13"/>
        <value type="int" value="7"/>
        <value type="int" value="11"/>
      </property>
      <property name="background-style" type="uint" value="1"/>
      <property name="enter-opacity" type="uint" value="100"/>
      <property name="leave-opacity" type="uint" value="100"/>
      <property name="background-rgba" type="array">
        <value type="double" value="{bg_r}"/>
        <value type="double" value="{bg_g}"/>
        <value type="double" value="{bg_b}"/>
        <value type="double" value="0.95"/>
      </property>
      <property name="background-image" type="string" value="file:///home/vinsho/it/arch-rice/src/wallpapers/cat.jpg"/>
      <property name="autohide-behavior" type="uint" value="0"/>
      <property name="length-adjust" type="bool" value="false"/>
      <property name="enable-struts" type="bool" value="false"/>
      <property name="nrows" type="uint" value="1"/>
      <property name="mode" type="uint" value="0"/>
      <property name="span-monitors" type="bool" value="true"/>
      <property name="output-name" type="string" value="Primary"/>
    </property>
  </property>
  <property name="plugins" type="empty">
    <property name="plugin-2" type="string" value="tasklist">
      <property name="grouping" type="bool" value="false"/>
      <property name="show-labels" type="bool" value="false"/>
      <property name="show-handle" type="bool" value="false"/>
      <property name="show-tooltips" type="bool" value="false"/>
      <property name="sort-order" type="uint" value="0"/>
      <property name="flat-buttons" type="bool" value="true"/>
      <property name="include-all-workspaces" type="bool" value="true"/>
      <property name="show-only-minimized" type="bool" value="false"/>
      <property name="include-all-monitors" type="bool" value="true"/>
    </property>
    <property name="plugin-3" type="string" value="separator">
      <property name="expand" type="bool" value="true"/>
      <property name="style" type="uint" value="0"/>
    </property>
    <property name="plugin-4" type="string" value="pager">
      <property name="rows" type="uint" value="1"/>
      <property name="wrap-workspaces" type="bool" value="false"/>
      <property name="miniature-view" type="bool" value="false"/>
    </property>
    <property name="plugin-5" type="string" value="separator">
      <property name="style" type="uint" value="0"/>
      <property name="expand" type="bool" value="true"/>
    </property>
    <property name="plugin-6" type="string" value="systray">
      <property name="square-icons" type="bool" value="true"/>
      <property name="known-legacy-items" type="array">
        <value type="string" value="wi-fi network connection “beach life” active: beach life (87%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (90%)"/>
        <value type="string" value="wi-fi network connection “apkuba” active: apkuba (67%)"/>
        <value type="string" value="wi-fi network connection “apkuba” active: apkuba (59%)"/>
        <value type="string" value="wi-fi network connection “apkuba” active: apkuba (63%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (69%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (80%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (70%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (54%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (66%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (59%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (58%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (57%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (67%)"/>
        <value type="string" value="wi-fi network connection “huawei-5552” active: huawei-5552 (89%)"/>
        <value type="string" value="wi-fi network connection “huawei-5552” active: huawei-5552 (62%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (79%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (83%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (86%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (82%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (85%)"/>
        <value type="string" value="wi-fi network connection “huawei-5552” active: huawei-5552 (67%)"/>
        <value type="string" value="requesting a wi-fi network address for “regiojet - zluty”…"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (88%)"/>
        <value type="string" value="networkmanager applet"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (84%)"/>
        <value type="string" value="requesting a wi-fi network address for “beach life”…"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (80%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (89%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (73%)"/>
        <value type="string" value="wi-fi network connection “beach life” active: beach life (81%)"/>
        <value type="string" value="wi-fi network connection “hub” active: hub (54%)"/>
        <value type="string" value="wi-fi network connection “huawei-5552” active: huawei-5552 (69%)"/>
        <value type="string" value="requesting a wi-fi network address for “huawei-5552”…"/>
        <value type="string" value="wi-fi network connection “huawei-5552” active: huawei-5552 (56%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (70%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (61%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (68%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (63%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (80%)"/>
        <value type="string" value="no network connection"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (69%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (72%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (77%)"/>
        <value type="string" value="requesting a wi-fi network address for “beach life 5g”…"/>
        <value type="string" value="ethernet network connection “wired connection 1” active"/>
        <value type="string" value="requesting an ethernet network address for “wired connection 1”…"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (76%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (71%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (74%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (73%)"/>
        <value type="string" value="wi-fi network connection “beach life 5g” active: beach life 5g (75%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (65%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (72%)"/>
        <value type="string" value="slack"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (69%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (68%)"/>
        <value type="string" value="wi-fi network connection “luda_net” active: luda_net (73%)"/>
        <value type="string" value="albert"/>
        <value type="string" value="flameshot"/>
      </property>
      <property name="known-items" type="array">
        <value type="string" value="flameshot"/>
        <value type="string" value="TelegramDesktop"/>
        <value type="string" value="chrome_status_icon_1"/>
        <value type="string" value="vlc"/>
        <value type="string" value="Yakuake"/>
        <value type="string" value="Microsoft Teams - Preview1"/>
        <value type="string" value="albert"/>
        <value type="string" value="blueman"/>
        <value type="string" value="Slack1"/>
      </property>
      <property name="hide-new-items" type="bool" value="false"/>
      <property name="icon-size" type="int" value="0"/>
      <property name="menu-is-primary" type="bool" value="false"/>
      <property name="hidden-items" type="array">
      </property>
      <property name="hidden-legacy-items" type="array">
      </property>
    </property>
    <property name="plugin-12" type="string" value="clock">
      <property name="mode" type="uint" value="2"/>
      <property name="digital-layout" type="uint" value="0"/>
      <property name="digital-time-format" type="string" value="%T"/>
      <property name="digital-date-format" type="string" value="%A, %B %d, %Y"/>
    </property>
    <property name="plugin-20" type="string" value="xkb">
      <property name="display-type" type="uint" value="0"/>
      <property name="display-name" type="uint" value="0"/>
      <property name="display-scale" type="uint" value="50"/>
      <property name="display-tooltip-icon" type="bool" value="false"/>
      <property name="group-policy" type="uint" value="0"/>
      <property name="show-notifications" type="bool" value="false"/>
      <property name="caps-lock-indicator" type="bool" value="true"/>
    </property>
    <property name="plugin-22" type="string" value="directorymenu">
      <property name="base-directory" type="string" value="/home/vinsho"/>
    </property>
    <property name="plugin-26" type="string" value="weather">
      <property name="location" type="empty">
        <property name="name" type="string" value="Brno, okres Brno-město"/>
        <property name="latitude" type="string" value="49.192244"/>
        <property name="longitude" type="string" value="16.611338"/>
      </property>
      <property name="msl" type="int" value="221"/>
      <property name="timezone" type="string" value="Europe/Prague"/>
      <property name="offset" type="string" value="+02:00"/>
      <property name="cache-max-age" type="int" value="172800"/>
      <property name="power-saving" type="bool" value="true"/>
      <property name="units" type="empty">
        <property name="temperature" type="int" value="0"/>
        <property name="pressure" type="int" value="0"/>
        <property name="windspeed" type="int" value="0"/>
        <property name="precipitation" type="int" value="0"/>
        <property name="altitude" type="int" value="0"/>
        <property name="apparent-temperature" type="int" value="0"/>
      </property>
      <property name="round" type="bool" value="true"/>
      <property name="single-row" type="bool" value="true"/>
      <property name="tooltip-style" type="int" value="1"/>
      <property name="forecast" type="empty">
        <property name="layout" type="int" value="1"/>
        <property name="days" type="int" value="5"/>
      </property>
      <property name="theme-dir" type="string" value="/usr/share/xfce4/weather/icons/liquid-dark"/>
      <property name="scrollbox" type="empty">
        <property name="show" type="bool" value="true"/>
        <property name="animate" type="bool" value="true"/>
        <property name="lines" type="int" value="1"/>
        <property name="color" type="string" value="rgba(0,0,0,0)"/>
        <property name="use-color" type="bool" value="false"/>
      </property>
    </property>
    <property name="plugin-1" type="string" value="pulseaudio">
      <property name="enable-keyboard-shortcuts" type="bool" value="true"/>
      <property name="known-players" type="string" value="Brave;Chrome;Firefox Web Browser;Spotify;VLC media player"/>
    </property>
    <property name="plugin-8" type="string" value="applicationsmenu">
      <property name="show-button-title" type="bool" value="false"/>
    </property>
    <property name="plugin-9" type="string" value="xfce4-clipman-plugin"/>
    <property name="plugin-13" type="string" value="actions">
      <property name="appearance" type="uint" value="1"/>
      <property name="button-title" type="uint" value="3"/>
      <property name="custom-title" type="string" value="⏻"/>
    </property>
    <property name="plugin-10" type="string" value="power-manager-plugin"/>
    <property name="plugin-7" type="string" value="xfce4-timer-plugin"/>
    <property name="plugin-11" type="string" value="xfce4-timer-plugin"/>
  </property>
</channel>"""
